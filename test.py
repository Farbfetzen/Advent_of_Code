#!/usr/bin/env python3

"""Running tests this way is necessary because unittest does not play nicely with argparse.
If I want to run the tests using the standard `python -m unittest` I cannot use custom
additional arguments for some reason. But I like using them to modify which tests to run
without having to define patterns for the test names (via the -k argument of unittest).

Run all the tests from the command line using `python test.py`
You can optionally specify a year to run all test from a year and additionally
a day to run the test of a specific day from one year.
Example:
- `python test.py 2021` runs all tests from 2021
- `python test.py 2021 3` runs all tests from day 3 of 2021
Use the optional argument -s or --skip-samples to skip all tests of sample inputs.
Use the optional argument -v or --verbosity combined with an integer to set
the verbosity of the test output. 0 is quiet, 1 is just the dots (default), and 2 is verbose.
Use -h or --help to see a help message about the arguments.
"""

from importlib import import_module
from unittest import defaultTestLoader, TestLoader, TextTestRunner

from src.util.check_python_version import check_python_version
from test.parse_test_args import parsed_args


def main() -> None:
    check_python_version()

    if parsed_args.day is None:
        loader = TestLoader()
        if parsed_args.year is None:
            test_suite = loader.discover("test")
        else:
            test_suite = loader.discover(f"test/year{parsed_args.year}")
    else:
        module = import_module(f"test.year{parsed_args.year}.test_day{parsed_args.day:02}")
        test_suite = defaultTestLoader.loadTestsFromModule(module)
    runner = TextTestRunner(verbosity=parsed_args.verbosity)
    runner.run(test_suite)


if __name__ == "__main__":
    main()
