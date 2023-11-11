import sys
import json
from utils.window_manager import WindowManager
from utils.process_launcher import ProcessLauncher
from config import DEFAULT_PROFILE_PATH

class WorkspaceAutomator:
    def __init__(self, profile_path=DEFAULT_PROFILE_PATH):
        self.profile = self._load_profile(profile_path)
        self.process_launcher = ProcessLauncher()
        self.window_manager = WindowManager(self.process_launcher)

    def _load_profile(self, profile_path):
        with open(profile_path, 'r') as f:
            return json.load(f)

    def launch_applications(self):
        for app in self.profile.get("applications", []):
            print(f"Processing app configuration: {app}")
            self.window_manager.position_window(app)

    def run(self):
        self.launch_applications()

def main(profile_path):
    automator = WorkspaceAutomator(profile_path)
    automator.run()

if __name__ == "__main__":
    profile_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PROFILE_PATH
    main(profile_path)
