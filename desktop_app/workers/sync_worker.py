"""
AVAGuard Desktop - Sync Worker Module

Background worker for synchronizing scans with the web portal.
"""

import logging
from PyQt6.QtCore import QThread, pyqtSignal
from utils.session_manager import GlobalSessionManager
from utils.exceptions import SessionRevokedError
from datetime import datetime

# Import web_client's own SessionRevokedException (different class, same purpose)
try:
    from web_client import SessionRevokedException
except ImportError:
    SessionRevokedException = None

logger = logging.getLogger(__name__)


def check_internet(host="8.8.8.8", port=53, timeout=3):
    """Check for internet connectivity asynchronously on worker thread."""
    import socket
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False


class SyncWorker(QThread):
    """
    Background worker for synchronizing scans.
    
    Signals:
        progress: Emitted with (current, total, status_text)
        finished: Emitted with (synced_count, failed_count, error_details)
        session_revoked: Emitted with error message when session is revoked
    """
    progress = pyqtSignal(int, int, str)
    finished = pyqtSignal(int, int, list)
    session_revoked = pyqtSignal(str)
    
    def __init__(self, db, web_client, unsynced_scans=None):
        super().__init__()
        self.db = db
        self.web_client = web_client
        self.unsynced_scans = unsynced_scans
        self.is_running = True
        
    def stop(self):
        self.is_running = False
        
    def run(self):
        synced_count = 0
        failed_count = 0
        error_details = []
        
        try:
            # 1. Revocation Guard
            if GlobalSessionManager().is_revoked():
                logger.info("Sync worker aborted: session is revoked")
                self.session_revoked.emit("Session revoked during sync")
                return

            if not self.is_running:
                return

            # 2. Internet Connection Check
            self.progress.emit(0, 1, "Checking connection...")
            if not check_internet():
                logger.warning("Sync worker skipped: no internet connection")
                self.finished.emit(0, 0, ["Sync skipped: no internet connection"])
                return

            if not self.is_running:
                return

            # 3. Authentication Status Check
            if not self.web_client.is_authenticated:
                logger.warning("Sync worker skipped: web client not authenticated")
                self.finished.emit(0, 0, ["Sync skipped: not authenticated"])
                return

            # 4. Session Validation Check
            self.progress.emit(0, 1, "Validating session...")
            try:
                valid = self.web_client.validate_session()
                if not valid:
                    logger.warning("Session validation returned False - skipping sync this cycle.")
                    self.finished.emit(0, 0, ["Sync skipped: session validation failed (will retry on next heartbeat)"])
                    return
            except Exception as e:
                is_revoked_exc = (
                    isinstance(e, SessionRevokedError)
                    or (SessionRevokedException and isinstance(e, SessionRevokedException))
                    or e.__class__.__name__ in ['SessionRevokedException', 'SessionRevokedError']
                )
                if is_revoked_exc:
                    logger.info("Session revoked response detected during sync validation.")
                    GlobalSessionManager().revoke()
                    self.session_revoked.emit("Session revoked by administrator")
                    return
                # General network timeout/errors -> continue optimistically to sync
                logger.warning(f"Sync session validation failed: {e}. Proceeding optimistically.")

            if not self.is_running:
                return

            # 5. Fetch Unsynced Scans from Database if not provided
            if self.unsynced_scans is None:
                self.progress.emit(0, 1, "Fetching unsynced scans...")
                self.unsynced_scans = self.db.get_unsynced_scans()

            if not self.unsynced_scans:
                self.progress.emit(1, 1, "All scans synced")
                self.finished.emit(0, 0, [])
                return

            total = len(self.unsynced_scans)
            logger.info(f"SyncWorker: Starting sync of {total} scan(s)")

            for i, scan in enumerate(self.unsynced_scans):
                if GlobalSessionManager().is_revoked():
                    logger.info(f"Sync cancellation started at {datetime.now().isoformat()}")
                    self.is_running = False
                    self.session_revoked.emit("Session revoked during sync")
                    logger.info(f"Sync cancellation ended at {datetime.now().isoformat()}")
                    return
                if not self.is_running:
                    break
                    
                scan_id = scan['scan_id']
                self.progress.emit(i, total, f"Syncing scan {scan_id[:8]}...")
                
                try:
                    # Get full details
                    details = self.db.get_scan_details(scan_id)
                    if not details:
                        failed_count += 1
                        error_details.append(f"Scan {scan_id[:8]}: No details found in local DB.")
                        continue

                    checks = details.get('checks', [])
                    
                    success, msg = self.web_client.upload_scan(
                        scan_id=scan_id,
                        overall_score=scan['overall_score'],
                        passed_count=scan['passed_checks'],
                        failed_count=scan['failed_checks'],
                        total_checks=scan['total_checks'],
                        results=checks
                    )
                    
                    if success:
                        self.db.mark_as_synced(scan_id)
                        synced_count += 1
                    else:
                        if GlobalSessionManager().is_revoked():
                            logger.info(f"Sync cancelled after revoked-session failure at {datetime.now().isoformat()}")
                            self.session_revoked.emit("Session revoked during sync (403 detected)")
                            return
                        failed_count += 1
                        clean_msg = str(msg)[:200]
                        error_details.append(f"Scan {scan_id[:8]}: {clean_msg}")
                        
                except Exception as e:
                    is_revoked_exc = (
                        isinstance(e, SessionRevokedError)
                        or (SessionRevokedException and isinstance(e, SessionRevokedException))
                        or e.__class__.__name__ in ['SessionRevokedException', 'SessionRevokedError']
                    )
                    if is_revoked_exc:
                        logger.info(f'Sync cancellation started (exception) at {datetime.now().isoformat()}')
                        GlobalSessionManager().revoke()
                        self.session_revoked.emit(str(e))
                        logger.info(f'Sync cancellation ended (exception) at {datetime.now().isoformat()}')
                        return
                    error_msg = f"Exception syncing {scan_id[:8]}: {str(e)}"
                    logger.error(error_msg)
                    failed_count += 1
                    error_details.append(error_msg)
                    
            if self.is_running:
                self.progress.emit(total, total, "Sync complete")
                self.finished.emit(synced_count, failed_count, error_details)

        except Exception as e:
            logger.exception("Unexpected error inside SyncWorker background thread")
            self.finished.emit(synced_count, failed_count + 1, [f"Fatal sync error: {e}"])
