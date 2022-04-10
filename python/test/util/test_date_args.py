from datetime import date
from unittest import TestCase

from parameterized import parameterized

from src.util.date_args import validate_date, validate_day, validate_year


class ValidateYearTest(TestCase):

    current_year: int

    @classmethod
    def setUpClass(cls) -> None:
        cls.current_year = date.today().year

    def test_earliest_year_works(self) -> None:
        try:
            validate_year(2015)
        except ValueError:
            self.fail("validate_year() raised ValueError unexpectedly!")

    def test_year_too_early(self) -> None:
        year = 2014
        with self.assertRaises(ValueError) as assertion_context:
            validate_year(year)
        self.assertEqual(
            str(assertion_context.exception),
            f"Year {year} not in range [2015, {self.current_year}]."
        )

    def test_year_too_late(self) -> None:
        year_late = self.current_year + 1
        with self.assertRaises(ValueError) as assertion_context:
            validate_year(year_late)
        self.assertEqual(
            str(assertion_context.exception),
            f"Year {year_late} not in range [2015, {self.current_year}]."
        )


class ValidateDayTest(TestCase):

    @parameterized.expand((("too early", 0), ("too late", 26)))
    def test_invalid_day(self, _, day) -> None:
        with self.assertRaises(ValueError) as assertion_context:
            validate_day(day)
        self.assertEqual(
            str(assertion_context.exception),
            f"Day {day} not in range [1, 25]."
        )


class ValidateDateTest(TestCase):

    def test_date_in_future(self) -> None:
        year = 2021
        day = 1
        today = date(year, 1, 1)
        with self.assertRaises(ValueError) as assertion_context:
            validate_date(year=year, day=day, today=today)
        self.assertEqual(
            str(assertion_context.exception),
            f"Date {date(year, 12, day)} is invalid because it's in the future."
        )
