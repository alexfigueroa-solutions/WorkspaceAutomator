import subprocess
import time
import win32api
import win32gui
import win32con
import pygetwindow as gw


class WindowManager:
    def __init__(self, process_launcher):
        self.process_launcher = process_launcher
        self.default_wait_time = 2

    def position_window(self, app):
        print(f"Positioning {app['name']}...")  # Debug print
        self.process_launcher.launch(app)
        time.sleep(self.default_wait_time)
        hwnd = self._get_window_handle(app["name"])

        if hwnd:
            self._move_window_to_monitor(hwnd, app["monitor"])
            self._maximize_window(hwnd)

    def _get_window_handle(self, title):
        try:
            window = gw.getWindowsWithTitle(title)[0]
            return window._hWnd
        except IndexError:
            return None

    def _move_window_to_monitor(self, hwnd, monitor_number):
        # Move the window off-screen to ensure it isn't maximized on the wrong monitor
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, -32000, -32000, 0, 0, win32con.SWP_SHOWWINDOW)
        time.sleep(0.5)  # Short delay for the window to move off-screen

        monitors = win32api.EnumDisplayMonitors()
        if monitor_number - 1 < len(monitors):
            monitor_info = win32api.GetMonitorInfo(monitors[monitor_number - 1][0])
            monitor_area = monitor_info['Monitor']
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, monitor_area[0], monitor_area[1], 0, 0, win32con.SWP_SHOWWINDOW)
        else:
            print("Monitor number out of range")

    def _maximize_window(self, hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)


# Main execution logic (not shown here) would create an instance of WorkspaceAutomator
# and call its run method, similar to what you have in your existing script.
