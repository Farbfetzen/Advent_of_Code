from unittest import TestCase

from src.util.load_data import load_data
from src.year2019.day04 import check_adjacent_pairs, check_adjacent_pairs_group, check_increasing_digits, \
    count_passwords, prepare_data
from test.decorators import sample


data = load_data(2019, 4)


@sample
class Test2019Day01Samples(TestCase):

    def test_111111(self) -> None:
        self.assertTrue(check_increasing_digits("111111") and check_adjacent_pairs("111111"))

    def test_223450(self) -> None:
        self.assertFalse(check_increasing_digits("223450") and check_adjacent_pairs("223450"))

    def test_123789(self) -> None:
        self.assertFalse(check_increasing_digits("123789") and check_adjacent_pairs("123789"))

    def test_112233(self) -> None:
        self.assertTrue(check_increasing_digits("112233") and check_adjacent_pairs_group("112233"))

    def test_123444(self) -> None:
        self.assertFalse(check_increasing_digits("123444") and check_adjacent_pairs_group("123444"))

    def test_111122(self) -> None:
        self.assertTrue(check_increasing_digits("111122") and check_adjacent_pairs_group("111122"))


class Test2019Day04(TestCase):

    prepared_data: list[int]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1_and_2(self) -> None:
        self.assertEqual((1650, 1129), count_passwords(self.prepared_data))
