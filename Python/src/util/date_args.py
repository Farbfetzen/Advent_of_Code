import argparse
import datetime
import sys


def add_date_args(parser: argparse.ArgumentParser) -> None:
    """Add optional, positional year and day arguments to the ArgumentParser."""
    parser.add_argument("year", type=int, nargs="?")
    parser.add_argument("day", type=int, nargs="?")


def validate_args(year: int | None, day: int | None) -> tuple[int, int]:
    """Check if year and day are both provided and valid.
    Returns the current date if none of them are provided.
    """
    today = datetime.date.today()
    if day is None:
        if year is None:
            year = today.year
            day = today.day
        else:
            sys.exit("Error: Either specify both year and day or none of them.")
    _validate_date(year, day, today)
    validate_year(year, today)
    validate_day(day)
    return year, day


def _validate_date(year: int, day: int, today: datetime.date) -> None:
    december_date = datetime.date(year, 12, day)
    if december_date > today:
        sys.exit(f"Error: Date {december_date} is invalid because it's in the future.")


def validate_year(year: int, today: datetime.date | None = None) -> None:
    today = today or datetime.date.today()
    if not (2015 <= year <= today.year):
        sys.exit(f"Error: Year {year} not in range [2015, {today.year}].")
    if year == today.year and today.month < 12:
        sys.exit(f"Error: Year {year} is invalid because it's not december yet.")


def validate_day(day: int) -> None:
    if not (1 <= day <= 25):
        sys.exit(f"Error: Day {day} not in range [1, 25].")
