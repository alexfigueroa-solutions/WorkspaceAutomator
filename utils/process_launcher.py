import subprocess

class ProcessLauncher:
    def launch(self, app):
        if "path" in app:
            command = [app["path"]]
        else:
            command = [app["command"]]

        arguments = app.get("arguments", [])
        print(f"Launching {app['command']}...")  # Debug print
        subprocess.Popen(command + arguments, shell=True)
