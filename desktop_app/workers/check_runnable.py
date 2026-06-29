"""
AVAGuard Desktop - Check Runnable Executor
Implements a threaded check executor using QRunnable, carrying performance telemetry instrumented hooks.
"""

import time
import logging
from typing import Dict, Any, Type, Optional
from dataclasses import dataclass

try:
    from PyQt6.QtCore import QRunnable, QObject, pyqtSignal
except ImportError:
    # CLI/Headless fallback
    class QRunnable:
        def run(self): pass
    class QObject:
        def __init__(self, *args, **kwargs): pass
    def pyqtSignal(*args, **kwargs):
        class DummySignal:
            def emit(self, *args, **kwargs): pass
        return DummySignal()

from avaguard_core.checks.base_check import CheckResult, CheckStatus, BaseCheck

logger = logging.getLogger(__name__)


@dataclass
class CheckTimingRecord:
    """Carries timing breakdowns for a single check run."""
    check_id: str
    init_duration_ms: float = 0.0
    execute_duration_ms: float = 0.0
    evidence_duration_ms: float = 0.0
    total_wall_time_ms: float = 0.0


class CheckRunnableSignals(QObject):
    """Signals carrier for CheckRunnable to interact with PyQt thread systems."""
    started = pyqtSignal(str)  # check_id
    completed = pyqtSignal(object, object)  # CheckResult, CheckTimingRecord
    rate_limited = pyqtSignal(str, float)  # provider_id, retry_after_seconds
    error = pyqtSignal(str, str)  # check_id, error_message


class CheckRunnable(QRunnable):
    """
    Thread-pool execution runnable for individual compliance checks.
    Provides detailed telemetry hooks and handles cloud rate throttling events.
    """
    def __init__(self, check_id: str, check_class: Type[BaseCheck], client: Any, config: Dict[str, Any]):
        super().__init__()
        self.check_id = check_id
        self.check_class = check_class
        self.client = client
        self.config = config
        self.signals = CheckRunnableSignals()

    def run(self):
        """Executes the check and gathers execution metrics."""
        self.signals.started.emit(self.check_id)
        
        timing = CheckTimingRecord(check_id=self.check_id)
        start_wall = time.perf_counter()
        
        # 1. Initialize stage
        init_start = time.perf_counter()
        check_instance = None
        try:
            # Attempt instantiation with config settings
            try:
                check_instance = self.check_class(self.client, config=self.config)
            except TypeError:
                # Fallback to old style without config parameter
                check_instance = self.check_class(self.client)
            timing.init_duration_ms = (time.perf_counter() - init_start) * 1000.0
        except Exception as e:
            timing.init_duration_ms = (time.perf_counter() - init_start) * 1000.0
            error_msg = f"Failed to instantiate check {self.check_id}: {str(e)}"
            logger.exception(error_msg)
            self._emit_error(error_msg, timing, start_wall)
            return

        # 2. Execution stage
        execute_start = time.perf_counter()
        try:
            result = check_instance.execute()
            timing.execute_duration_ms = (time.perf_counter() - execute_start) * 1000.0
            
            # Double check result object type
            if not isinstance(result, CheckResult):
                raise ValueError(f"Returned object must be CheckResult, got: {type(result)}")
                
            # If not assigned, assign check_id
            if not hasattr(result, 'check_id') or not result.check_id:
                result.check_id = self.check_id
                
            # Update check duration in results
            result.duration_seconds = timing.execute_duration_ms / 1000.0
            
            # Rate limit/Throttling detection:
            # Standard HTTP 429 response contains 'retry-after' or rate limit info
            # Check if result status is ERROR or WARNING and check error message for throttling indicators
            is_throttled = False
            retry_after = 2.0  # Default cooldown
            
            error_text = str(getattr(result, 'error_message', '') or '').lower()
            details_text = str(getattr(result, 'details', '') or '').lower()
            
            if "429" in error_text or "too many requests" in error_text or "429" in details_text or "too many requests" in details_text:
                is_throttled = True
                # Attempt to parse retry_after value if present
                for text in [error_text, details_text]:
                    if "retry-after" in text or "retry" in text:
                        import re
                        match = re.search(r'(?:retry-after|retry\s+after|in)\s*(?:of)?\s*(\d+)\s*(?:s|sec|seconds)?', text)
                        if match:
                            try:
                                retry_after = float(match.group(1))
                            except ValueError:
                                pass
                            break
            
            if is_throttled:
                provider_id = self.config.get("provider_id", "azure")
                logger.warning(f"Detected 429 Rate Throttling on check {self.check_id} for provider {provider_id}. Retry-after: {retry_after}s.")
                self.signals.rate_limited.emit(provider_id, retry_after)
                
            # 3. Evidence classification stage (hook placeholders)
            evidence_start = time.perf_counter()
            # In Phase B.3 this hooks into the classification/encryption module
            timing.evidence_duration_ms = (time.perf_counter() - evidence_start) * 1000.0
            
            # Complete wall time
            timing.total_wall_time_ms = (time.perf_counter() - start_wall) * 1000.0
            self.signals.completed.emit(result, timing)

        except Exception as e:
            timing.execute_duration_ms = (time.perf_counter() - execute_start) * 1000.0
            error_msg = f"Check {self.check_id} crashed during execution: {str(e)}"
            logger.exception(error_msg)
            self._emit_error(error_msg, timing, start_wall)

    def _emit_error(self, error_msg: str, timing: CheckTimingRecord, start_wall: float):
        """Creates and emits an error result."""
        timing.total_wall_time_ms = (time.perf_counter() - start_wall) * 1000.0
        
        # Formulate fallback CheckResult
        title = getattr(self.check_class, 'TITLE', 'Unknown Check')
        error_result = CheckResult(
            check_id=self.check_id,
            title=title,
            status=CheckStatus.ERROR,
            details=f"Execution failure: {error_msg}",
            error_message=error_msg,
            compliant_count=0,
            non_compliant_count=0,
            total_count=0
        )
        error_result.duration_seconds = timing.total_wall_time_ms / 1000.0
        
        self.signals.error.emit(self.check_id, error_msg)
        self.signals.completed.emit(error_result, timing)
