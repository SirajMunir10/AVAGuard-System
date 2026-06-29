import sys
import os
import unittest.mock

# Resolve absolute paths
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
sys.path.insert(0, os.path.dirname(project_root))

# Create functional mock QObject & signals for headless testing
class MockQObject:
    def __init__(self, *args, **kwargs):
        pass
    def parent(self):
        return None
    def setParent(self, parent):
        pass

class MockPyqtSignal:
    def __init__(self, *args, **kwargs):
        pass
    def emit(self, *args, **kwargs):
        pass
    def connect(self, *args, **kwargs):
        pass
    def disconnect(self, *args, **kwargs):
        pass

def pyqtSignal(*args, **kwargs):
    return MockPyqtSignal()

import threading

class MockQThread(MockQObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._thread = None
        
    def start(self):
        if hasattr(self, 'run'):
            self._thread = threading.Thread(target=self.run)
            self._thread.start()
            
    def wait(self, timeout=None):
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=timeout)
            
    def isFinished(self):
        return self._thread is None or not self._thread.is_alive()

# Create structured mock QtCore module
mock_qtcore = unittest.mock.MagicMock()
mock_qtcore.QObject = MockQObject
mock_qtcore.pyqtSignal = pyqtSignal
mock_qtcore.QThread = MockQThread
mock_qtcore.QRunnable = object  # Avoid mock inheritance overhead for runnable
mock_qtcore.QTimer = unittest.mock.MagicMock
mock_qtcore.QSize = unittest.mock.MagicMock
mock_qtcore.QUrl = unittest.mock.MagicMock

sys.modules['PyQt6'] = unittest.mock.MagicMock()
sys.modules['PyQt6.QtWidgets'] = unittest.mock.MagicMock()
sys.modules['PyQt6.QtCore'] = mock_qtcore
sys.modules['PyQt6.QtGui'] = unittest.mock.MagicMock()
sys.modules['ui'] = unittest.mock.MagicMock()
