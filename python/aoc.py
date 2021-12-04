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
    raise ValueError(f"Year {year} not in range [2015, {today.year}].")
if not (1 <= day <= 25):
    raise ValueError(f"Day {day} not in range [1, 25].")

year = str(year)
day = f"{day:02}"
base_path = os.path.dirname(os.path.realpath(__file__))
year_dir = os.path.join(base_path, year)
input_filename = f"{year}-{day}-input.txt"
sample_filename = input_filename.replace("input.txt", "sample.txt")
relative_input_path = os.path.join("..", "..", "input", input_filename)
relative_sample_path = os.path.join("..", "..", "input", sample_filename)
input_path = os.path.abspath(os.path.join(base_path, "..", "input", input_filename))
sample_path = input_path.replace(input_filename, sample_filename)
solution_path = os.path.join(year_dir, f"day{day}.py")
test_path = os.path.join(year_dir, f"test{year}.py")
config_path = os.path.abspath(os.path.join(base_path, "..", "config.json"))

challenge_url = f"https://adventofcode.com/{year}/day/{day}"
input_url = challenge_url + "/input"

solution_template = f"""# {challenge_url}\n\n
def get_data(filename):
    with open(filename) as file:
        return file.read().splitlines()\n\n
def part_1(foo):
    pass\n\n
# def part_2(foo):
#     pass\n\n
sample_data = get_data("{relative_sample_path}")
challenge_data = get_data("{relative_input_path}")\n
if __name__ == "__main__":
    assert part_1(sample_data)
    # assert part_2(sample_data)\n
    print(part_1(challenge_data))  #
    # print(part_2(challenge_data))  #
"""

test_template = f"""import unittest\n
import day{day}\n\n
class Test{year}(unittest.TestCase):\n
    def test_{day}(self):
        self.assertEqual(day{day}.part_1(day{day}.sample_data), 0)
        # self.assertEqual(day{day}.part_2(day{day}.sample_data), 0)\n
        self.assertEqual(day{day}.part_1(day{day}.challenge_data), 0)
        # self.assertEqual(day{day}.part_2(day{day}.challenge_data), 0)\n\n
if __name__ == "__main__":
    unittest.main()
"""

if not os.path.exists(year_dir):
    os.mkdir(year_dir)

if os.path.exists(solution_path):
    print("Skipping script generation because it already exists.")
else:
    print("Writing script file.")
    with open(solution_path, "w") as file:
        file.write(solution_template)

if os.path.exists(sample_path):
    print("Skipping sample file generation because it already exists.")
else:
    print("Writing sample file.")
    open(sample_path, "w").close()

if os.path.exists(input_path):
    print("Skipping input file generation because it already exists.")
else:
    print("Downloading input.")
    # Remember that the session cookie expires after a month. You can get
    # the current one from the website while being logged in.
    # Right click -> Inspect Element -> Storage tab
    with open(config_path) as file:
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

if os.path.exists(test_path):
    print("Skipping test file generation because it already exists.")
else:
    print("Writing test file.")
    with open(test_path, "w") as file:
        file.write(test_template)

print("Done. Have fun!\n")

# These links should be clickable in the console.
print(f"file://{os.path.abspath(solution_path)}")
print(f"file://{os.path.abspath(sample_path)}")
print(f"file://{os.path.abspath(input_path)}")
print(f"file://{os.path.abspath(test_path)}")
print(challenge_url)
