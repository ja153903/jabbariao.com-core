import subprocess


def main():
    cmd = ["python", "manage.py", "runserver"]
    subprocess.run(cmd)
