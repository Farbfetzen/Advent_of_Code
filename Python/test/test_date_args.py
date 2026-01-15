import datetime
from typing import Self

import pytest

from src.util import date_args


current_year = datetime.date.today().year


def mock_today(today: datetime.date, monkeypatch) -> None:
    class MyDatetime(datetime.date):
        @classmethod
        def today(cls) -> Self:
            return today

    monkeypatch.setattr(datetime, "date", MyDatetime)


def test_validate_args(monkeypatch) -> None:
    mock_today(datetime.date(2025, 12, 25), monkeypatch)
    assert (2024, 1) == date_args.validate_args(2024, 1)


def test_validate_args_none(monkeypatch) -> None:
    mock_today(datetime.date(2024, 12, 1), monkeypatch)
    assert (2024, 1) == date_args.validate_args(None, None)


def test_invalid_args() -> None:
    with pytest.raises(SystemExit) as exception:
        date_args.validate_args(1, None)
    assert str(exception.value) == "Error: Either specify both year and day or none of them."


def test_date_in_future(monkeypatch) -> None:
    mock_today(datetime.date(2021, 1, 1), monkeypatch)
    with pytest.raises(SystemExit) as exception:
        date_args.validate_args(2021, 1)
    assert str(exception.value) == "Error: Date 2021-12-01 is invalid because it's in the future."


def test_valid_year() -> None:
    for year in range(2015, current_year):
        date_args.validate_year(year)


@pytest.mark.parametrize("year", [2014, current_year + 1])
def test_year_too_early(year: int) -> None:
    with pytest.raises(SystemExit) as exception:
        date_args.validate_year(year)
    assert str(exception.value) == f"Error: Year {year} not in range [2015, {current_year}]."


def test_not_december_yet() -> None:
    with pytest.raises(SystemExit) as exception:
        date_args.validate_year(2024, datetime.date(2024, 1, 1))
    assert str(exception.value) == "Error: Year 2024 is invalid because it's not december yet."


def test_valid_day() -> None:
    for day in range(1, 26):
        date_args.validate_day(day)


@pytest.mark.parametrize("day", [0, 26])
def test_invalid_day(day) -> None:
    with pytest.raises(SystemExit) as exception:
        date_args.validate_day(day)
    assert str(exception.value) == f"Error: Day {day} not in range [1, 25]."
