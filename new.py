"""Creates a script with some boilerplate code and downloads the input
for a given day. The optional arguments are 'year' and 'day' with the
current year and day as default values.
Example: python new.py 2020 7
"""


import argparse
import datetime
import json
import os
import requests


today = datetime.date.today()
parser = argparse.ArgumentParser()
parser.add_argument("year", type=int, default=today.year, nargs="?")
parser.add_argument("day", type=int, default=today.day, nargs="?")
args = parser.parse_args()
year = args.year
day = args.day
if not (2015 <= year <= today.year):
    raise ValueError(f"Year {year} outside of sensible range.")
if not (1 <= day <= 25):
    raise ValueError(f"Day {day} outside of sensible range.")

year = str(year)
base_path = f"day_{day:02}"
script_path = os.path.join(year, base_path + ".py")
relative_input_path = base_path + "_input.txt"
input_path = os.path.join(year, relative_input_path)
challenge_url = f"https://adventofcode.com/{year}/day/{day}"
input_url = challenge_url + "/input"

if not os.path.exists(year):
    os.mkdir(year)

script_content = f'''# {challenge_url}\n\n
import collections
import math
import numpy
from pprint import pprint\n\n
def part_1(foo):
    return 0\n\n
def part_2(foo):
    return 0\n\n
test_input = """\\
""".splitlines()
# assert part_1(test_input) ==
# assert part_2(test_input) ==\n\n
with open("{relative_input_path}") as file:
    challenge_input = file.read().splitlines()
# print(part_1(challenge_input))  #
# print(part_2(challenge_input))  #
'''
if os.path.exists(script_path):
    print("Skipping script generation because the file already exists.")
else:
    print("Writing script file.")
    with open(script_path, "w") as file:
        file.write(script_content)

if os.path.exists(input_path):
    print("Skipping input file generation because the file already exists.")
else:
    print("Downloading input.")
    # Remember that the session cookie expires after a month. You can get
    # the current one from the website while being logged in.
    # Right click -> Inspect Element -> Storage tab
    with open("config.json") as file:
        config = json.load(file)
    cookie = config["session_cookie"]

    req = requests.get(input_url, cookies={"session": cookie}, timeout=5)
    if not req.ok:
        print("Error! Got status:", req.status_code)
        print(req.text)

    print("Writing input file.")
    with open(input_path, "w") as file:
        if req.ok:
            file.write(req.text)
        # else the file remains empty and the input should be pasted manually

print("Done. Have fun!\n")

# Print links to the files that should be clickable in the console.
print(f"file://{os.path.abspath(script_path)}")
print(f"file://{os.path.abspath(input_path)}")
print(challenge_url)
