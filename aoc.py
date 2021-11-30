#!/usr/bin/env python3

"""Creates a script with some boilerplate code and downloads the input
for a given day. The optional arguments are 'year' and 'day' with the
current year and day as default values.
Example: ./aoc.py 2020 7
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
sample_path = input_path.replace("input", "sample")
challenge_url = f"https://adventofcode.com/{year}/day/{day}"
input_url = challenge_url + "/input"
test_path = os.path.join(year, f"test_{year}.py")

if not os.path.exists(year):
    os.mkdir(year)

script_template = f'''# {challenge_url}\n\n
def get_data(filename):
    with open(filename) as file:
        return file.read().splitlines()\n\n
def part_1(foo):
    pass\n\n
# def part_2(foo):
#     pass\n\n
sample_data = get_data("{base_path}_sample.txt")
challenge_data = get_data("{base_path}_input.txt")\n
if __name__ == "__main__":
    assert part_1(sample_data)
    # assert part_2(sample_data)\n
    print(part_1(challenge_data))
    # print(part_2(challenge_data))\n
'''

if os.path.exists(script_path):
    print("Skipping script generation because the file already exists.")
else:
    print("Writing script file.")
    with open(script_path, "w") as file:
        file.write(script_template)

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

    response = requests.get(input_url, cookies={"session": cookie}, timeout=5)
    if not response.ok:
        print("Error! Got status:", response.status_code)
        print(response.text)

    print("Writing input file.")
    with open(input_path, "w") as file:
        if response.ok:
            file.write(response.text)
        # Else the file remains empty and the input should be pasted manually.

if os.path.exists(sample_path):
    print("Skipping sample file generation because the file already exists.")
else:
    print("Writing sample file.")
    open(sample_path, "w").close()

print("Done. Have fun!\n")

# These links should be clickable in the console.
print(f"file://{os.path.abspath(script_path)}")
print(f"file://{os.path.abspath(input_path)}")
print(f"file://{os.path.abspath(sample_path)}")
print(f"file://{os.path.abspath(test_path)}")
print(challenge_url)
