#!/usr/bin/env python3

from argparse import ArgumentParser
from importlib import import_module
from typing import cast

# noinspection PyUnresolvedReferences
import src.util.check_python_version
from src.util.date_args import add_date_args, validate_args_default_today
from src.util.load_data import load_data
from src.util.types import ModuleWithSolveFunction


def main() -> None:
    parser = ArgumentParser()
    add_date_args(parser)
    args = parser.parse_args()
    year, day = validate_args_default_today(args.year, args.day)

    data = load_data(year, day)
    solution_module = cast(ModuleWithSolveFunction, import_module(f"src.year{year}.day{day:02}"))
    solution = solution_module.solve(data)

    print(solution)


if __name__ == "__main__":
    main()
