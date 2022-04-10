"""Must be imported before all other modules or else the interpreter
might become upset about some type hints.
"""

import os
import sys


base_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(base_path, "..", "..", "requirements.txt")) as file:
    for line in file:
        if "Python version" in line:
            version = line.split(":")[1]
            break
major, minor = version.split(".")
major = int(major)
minor = int(minor)
if sys.version_info < (major, minor):
    raise SystemExit(f"This project requires Python version {major}.{minor} or above.")
