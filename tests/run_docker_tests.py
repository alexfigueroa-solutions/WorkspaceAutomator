import os
import subprocess

def build_docker_image():
    cmd = [
        "docker", "build",
        "-t", "gui-tester",
        "-f", "Dockerfile.gui",
        "."
    ]
    subprocess.run(cmd, check=True)

def run_docker_container():
    xauth_path = os.path.expanduser("~/.Xauthority")
    cmd = ["docker", "run", "--rm",
        "-v", f"{os.getcwd()}/tests/..:/app",
        "-v", f"{xauth_path}:/root/.Xauthority",
        "-e", "DISPLAY=unix:99",
        "gui-tester", "/app/run_tests.sh"]

    subprocess.run(cmd, check=True)

def main():
    build_docker_image()
    run_docker_container()

if __name__ == "__main__":
    main()
