import pytest
from unittest.mock import patch
from utils.process_launcher import ProcessLauncher

def test_process_launcher():
    launcher = ProcessLauncher()

    # Mocking the subprocess call
    with patch('utils.process_launcher.subprocess.Popen') as mocked_popen:
        app = {"path": "dummy_path"}
        launcher.launch(app)
        mocked_popen.assert_called_once_with(["dummy_path"], shell=True)
