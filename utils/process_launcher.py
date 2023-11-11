import subprocess

class ProcessLauncher:
    def launch(self, app):
        if "path" in app:
            command = [app["path"]]
        else:
            command = [app["command"]]

        arguments = app.get("arguments", [])
        print(f"Launching {app['name']} with command: {command + arguments}")  # Enhanced logging
        subprocess.Popen(command + arguments, shell=True)
