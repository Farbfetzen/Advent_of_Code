from unittest import TestCase

from src.util.load_data import load_data
from src.year2020.day15 import play, prepare_data


data = load_data(2020, 15)


class Test2020Day15(TestCase):

    prepared_data: list[int]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(240, play(self.prepared_data, 2020))

    def test_part_2(self) -> None:
        self.assertEqual(505, play(self.prepared_data, 30_000_000))
