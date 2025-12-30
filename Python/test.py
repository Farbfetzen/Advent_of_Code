#!/usr/bin/env python3

"""Running tests this way is not necessary but makes it easier to specify a year or day to test.
You can also run pytest directly, see https://docs.pytest.org/en/stable/how-to/usage.html#how-to-invoke-pytest.

Run all the tests from the command line using `python test.py`
You can optionally specify a year to run all test from a year
and additionally a day to run the tests of a specific day from one year.
If more than one day is specified the days are run in parallel.
Example:
- `python test.py` runs all tests in parallel
- `python test.py 2021` runs all tests from 2021 in parallel
- `python test.py 2021 3` runs all tests from day 3 of 2021
"""
import argparse

import pytest

from src.util import date_args


parser = argparse.ArgumentParser()
date_args.add_date_args(parser)
args = parser.parse_args()
year = args.year
day = args.day

# "-n auto" is from pytest-xdist for parallel test execution.
# Single days are not run in parallel because setup fixtures are module scoped.
# Multiple workers would just waste time in this case.
if year:
    date_args.validate_year(year)
    if day:
        date_args.validate_day(day)
        pytest.main([f"test/test_{year}.py::test_day_{day:02}"])
    else:
        pytest.main(["-n", "auto", f"test/test_{year}.py"])
else:
    pytest.main(["-n", "auto", "test"])
