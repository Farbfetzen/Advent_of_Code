from argparse import ArgumentParser
from datetime import date
from typing import Optional


def add_date_args(parser: ArgumentParser) -> None:
    """Add optional, positional year and day arguments to the ArgumentParser."""
    parser.add_argument("year", type=int, nargs="?")
    parser.add_argument("day", type=int, nargs="?")


def validate_args_default_today(year: int, day: int) -> tuple[int, int]:
    today = date.today()
    if day is None:
        if year is None:
            year = today.year
            day = today.day
        else:
            raise ValueError("Either specify both year and day or none of them.")
    validate_date(year, day, today)
    validate_year(year, today)
    validate_day(day)
    return year, day


def validate_date(year: int, day: int, today: Optional[date] = None) -> None:
    today = today or date.today()
    december_date = date(year, 12, day)
    if december_date > today:
        raise ValueError(f"Date {december_date} is invalid because it's in the future.")


def validate_year(year: int, today: Optional[date] = None) -> None:
    today = today or date.today()
    if not (2015 <= year <= today.year):
        raise ValueError(f"Year {year} not in range [2015, {today.year}].")
    if year == today.year and today.month < 12:
        raise ValueError(f"Year {year} is invalid because it's not december yet.")


def validate_day(day: int) -> None:
    if not (1 <= day <= 25):
        raise ValueError(f"Day {day} not in range [1, 25].")
