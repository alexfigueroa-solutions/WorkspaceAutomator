import subprocess
import time
import win32api
import win32gui
import win32con
import pygetwindow as gw
class WindowManager:
    def __init__(self, process_launcher):
        self.process_launcher = process_launcher
        self.timeout = 10  # Maximum time to wait for the window to appear in seconds
        self.handled_hwnds = set()  # Track HWNDs of handled windows

    def position_window(self, app):
        print(f"Positioning {app['name']}...")
        self.process_launcher.launch(app)
        hwnd = self._wait_for_window_handle(app["name"])

        if hwnd:
            self._move_window_to_monitor(hwnd, app["monitor"])
            if app.get("maximize", True):
                self._maximize_window(hwnd)
        else:
            print(f"Failed to find window for {app['name']} within timeout.")

    def _wait_for_window_handle(self, title):
        start_time = time.time()
        while time.time() - start_time < self.timeout:
            hwnd = self._get_window_handle(title)
            if hwnd:
                return hwnd
            time.sleep(0.2)  # Check every 0.5 seconds
        return None

    def _get_window_handle(self, title):
        windows = gw.getWindowsWithTitle(title)
        for window in windows:
            hwnd = window._hWnd
            if hwnd not in self.handled_hwnds:
                self.handled_hwnds.add(hwnd)  # Add to tracked HWNDs
                return hwnd
        return None

    def _move_window_to_monitor(self, hwnd, monitor_number):
        print(f"Preparing to move window (HWND: {hwnd}) to monitor {monitor_number}")

        # Check if the window is maximized using GetWindowPlacement
        window_placement = win32gui.GetWindowPlacement(hwnd)
        is_maximized = window_placement[1] == win32con.SW_SHOWMAXIMIZED
        print(f"Window is {'maximized' if is_maximized else 'not maximized'}")

        # Move the window off-screen (if not maximized)
        if not is_maximized:
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, -32000, -32000, 0, 0, win32con.SWP_SHOWWINDOW)
            print("Window moved off-screen")
            time.sleep(0.2)  # Reduced sleep time

        # Enumerate monitors and move the window to the desired monitor
        monitors = win32api.EnumDisplayMonitors()
        if monitor_number - 1 < len(monitors):
            monitor_info = win32api.GetMonitorInfo(monitors[monitor_number - 1][0])
            monitor_area = monitor_info['Monitor']
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, monitor_area[0], monitor_area[1], 0, 0, win32con.SWP_SHOWWINDOW)
            print(f"Window moved to monitor {monitor_number}")
            time.sleep(0.2)  # Reduced sleep time
        else:
            print("Monitor number out of range")

        # Restore the window to its original state (if it was maximized)
        if is_maximized:
            win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
            print("Window restored to maximized state")

    def _maximize_window(self, hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
