from unittest import TestCase

from parameterized import parameterized

from src.util.load_data import load_data
from src.year2020.day05 import get_seat_id, part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2020, 5)


class Test2020Day05(TestCase):

    prepared_data: list[int]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    @parameterized.expand(((0, 357), (1, 567), (2, 119), (3, 820)))
    @sample
    def test_get_seat_id(self, i, expected) -> None:
        self.assertEqual(expected, get_seat_id(data.samples[i]))

    def test_part_1(self) -> None:
        self.assertEqual(848, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(682, part_2(self.prepared_data))
