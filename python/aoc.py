#!/usr/bin/env python3

import argparse
import sys

from src import solutions
from src.util.inputs import load_inputs


parser = argparse.ArgumentParser()
parser.add_argument("year", type=int)
parser.add_argument("day", type=int)
args = parser.parse_args()
year = args.year
day = args.day

try:
    solution = solutions[year][day]()
except KeyError:
    sys.exit(f"Error: No solution found for {year=}, {day=}.")

inputs = load_inputs(year, day)
solution.solve(inputs)
print(solution)
