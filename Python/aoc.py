#!/usr/bin/env python3

from argparse import ArgumentParser

from src import solutions
from src.util.check_python_version import check_python_version
from src.util.date_args import add_date_args, validate_args_default_today
from src.util.load_inputs import load_inputs


if __name__ == "__main__":
    check_python_version()
    parser = ArgumentParser()
    add_date_args(parser)
    args = parser.parse_args()
    year, day = validate_args_default_today(args.year, args.day)

    inputs = load_inputs(year, day)
    solution = solutions[year][day]()
    solution.solve(inputs)
    print(solution)
