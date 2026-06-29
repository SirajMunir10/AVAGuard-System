"""
AVAGuard Core — Benchmarks Package
"""

from avaguard_core.benchmarks.models import (
    ScanQuerySpec,
    EvaluationRuleSpec,
    RemediationTemplatesSpec,
    RemediationMetadataSpec,
    ControlDefinition,
    BenchmarkVersion
)
from avaguard_core.benchmarks.loader import BenchmarkLoader

__all__ = [
    'ScanQuerySpec',
    'EvaluationRuleSpec',
    'RemediationTemplatesSpec',
    'RemediationMetadataSpec',
    'ControlDefinition',
    'BenchmarkVersion',
    'BenchmarkLoader'
]
