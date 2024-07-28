from unittest import TestCase

from src.util.load_data import load_data
from src.year2020.day24 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2020, 24)


@sample
class Test2020Day24Samples(TestCase):

    sum_black: int
    tiles: set[complex]

    @classmethod
    def setUpClass(cls) -> None:
        prepared_data = prepare_data(data.samples[0])
        cls.sum_black, cls.tiles = part_1(prepared_data)

    def test_part_1(self) -> None:
        self.assertEqual(10, self.sum_black)

    def test_part_2(self) -> None:
        self.assertEqual(2208, part_2(self.tiles))


class Test2020Day24(TestCase):

    sum_black: int
    tiles: set[complex]

    @classmethod
    def setUpClass(cls) -> None:
        prepared_data = prepare_data(data.input)
        cls.sum_black, cls.tiles = part_1(prepared_data)

    def test_part_1(self) -> None:
        self.assertEqual(528, self.sum_black)

    def test_part_2(self) -> None:
        self.assertEqual(4200, part_2(self.tiles))
