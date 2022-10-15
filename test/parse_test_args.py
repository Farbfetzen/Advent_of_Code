from argparse import ArgumentParser, Namespace
from typing import NamedTuple

from src.util import date_args


class ParsedArgs(NamedTuple):

    year: int
    day: int
    skip_samples: bool
    verbosity: int


def _parse_year_day(args: Namespace) -> tuple[int, int]:
    year = args.year
    day = args.day
    if year is not None:
        date_args.validate_year(year)
    if day is not None:
        date_args.validate_day(day)
    return year, day


def _parse_args() -> ParsedArgs:
    parser = ArgumentParser()
    date_args.add_date_args(parser)
    parser.add_argument("-s", "--skip-samples", action="store_true")
    parser.add_argument(
        "-v",
        "--verbosity",
        type=int,
        default=1,
        help="Verbosity of the test output. 0 is quiet, 1 is just the dots (default), and 2 is verbose.")
    args = parser.parse_args()
    year, day = _parse_year_day(args)
    return ParsedArgs(year=year, day=day, skip_samples=args.skip_samples, verbosity=args.verbosity)


parsed_args = _parse_args()
