import pyautogui
import pygetwindow as gw
import time

class WindowManager:
    def position_window(self, app):
        # Handle monitor selection and switch to the desired monitor
        self._switch_monitor(app["monitor"])

        # Wait for the application window to appear and get its title
        time.sleep(2)
        window = self._get_window_by_title(app["name"])

        # Handle window positioning
        if type(app["position"]) is dict:
            self._position_window_by_coordinates(window, app["position"])
        else:
            self._position_window_by_keyword(window, app["position"])

        # Handle workspace shift if provided
        if "workspace" in app:
            self._switch_workspace(app["workspace"])

    def _switch_monitor(self, monitor_number):
        # For simplicity, we'll just move the mouse to the desired monitor
        # You can enhance this logic further
        if monitor_number == 1:
            pyautogui.moveTo(0, 0)
        else:
            pyautogui.moveTo(pyautogui.size().width / 2, 0)

    def _position_window_by_coordinates(self, window, position):
        # Adjust the window size and position
        screen_width, screen_height = pyautogui.size()
        width = position["width"] if type(position["width"]) is int else int(screen_width * float(position["width"].strip('%')) / 100)
        height = position["height"] if type(position["height"]) is int else int(screen_height * float(position["height"].strip('%')) / 100)
        window.resizeTo(width, height)
        window.moveTo(position["left"], position["top"])

    def _position_window_by_keyword(self, window, position_keyword):
        if position_keyword == "maximized":
            window.maximize()

    def _switch_workspace(self, workspace_number):
        # Assuming Ctrl + Win + Left/Right switches workspaces
        for _ in range(workspace_number - 1):
            pyautogui.hotkey('ctrl', 'win', 'right')

    def _get_window_by_title(self, title):
        for window in gw.getWindowsWithTitle(''):
            if title.lower() in window.title.lower():
                return window
        return None
