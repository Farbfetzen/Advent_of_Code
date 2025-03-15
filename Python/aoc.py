#!/usr/bin/env python3

import argparse
import sys

from src import solutions
from src.util import date_args
from src.util.check_python_version import check_python_version
from src.util.inputs import load_inputs


check_python_version()
parser = argparse.ArgumentParser()
date_args.add_date_args(parser)
args = parser.parse_args()
year, day = date_args.validate_args(args.year, args.day)

try:
    solution = solutions[year][day]()
except KeyError:
    sys.exit(f"Error: No solution exists for {year=}, {day=}. Did you forget to add it to src/year_{year}/__init__.py?")

inputs = load_inputs(year, day)
solution.solve(inputs)
print(solution)
