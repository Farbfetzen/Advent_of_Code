from unittest import TestCase

from src.util.load_data import load_data
from src.year2018.day01 import part_1, part_2, prepare_data


data = load_data(2018, 1)


class Test2018Day01(TestCase):

    prepared_data: list[int]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(561, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(563, part_2(self.prepared_data))
