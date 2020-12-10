"""Creates script and input files for a given day and fills the script
with some boilerplate code. Takes year and day as arguments, like this:
python new.py 2020 7
"""


import sys
import os


if len(sys.argv) != 3:
    raise IndexError(
        "Need exactly two arguments: year and day. Example:\n"
        "'python new.py 2020 7'"
    )

year = sys.argv[1]
day = sys.argv[2]
if not year.isdecimal() or not day.isdecimal():
    raise ValueError("Year and day must be integers.")

base_path = f"day_{day.rjust(2, '0')}"
script_path = os.path.join(year, base_path + ".py")
relative_input_path = base_path + "_input.txt"
input_path = os.path.join(year, relative_input_path)

if os.path.exists(script_path) or os.path.exists(input_path):
    raise OSError("One or both files already exist.")

if not os.path.exists(year):
    os.makedirs(year)

script_content = f'''\
# https://adventofcode.com/{year}/day/{day}


import collections
import math
import numpy
from pprint import pprint


def part_1(foo):
    return 0


def part_2(bar):
    return 0


test_input = """
""".splitlines()
# assert part_1(test_input) == 
# assert part_2(test_input) == 


with open("{relative_input_path}") as file:
    challenge_input = file.read().splitlines()
# print(part_1(challenge_input))  # 
# print(part_2(challenge_input))  # 
'''
with open(script_path, "w") as file:
    file.write(script_content)

with open(input_path, "w") as file:
    pass  # empty file
