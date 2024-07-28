import os
import sys


def check_python_version():
    base_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(base_path, "..", "..", "requirements.txt")) as file:
        for line in file:
            if "Python version" in line:
                version = line.split(":")[1]
                break
    major, minor = (int(x) for x in version.split("."))
    if sys.version_info < (major, minor):
        raise SystemExit(f"This project requires Python version {major}.{minor} or above.")
