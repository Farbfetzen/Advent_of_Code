from unittest import TestCase

from src.util.load_data import load_data
from src.year2022.day04 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2022, 4)


@sample
class Test2022Day04Samples(TestCase):

    prepared_data: list[list[int]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(2, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(4, part_2(self.prepared_data))


class Test2022Day04(TestCase):

    prepared_data: list[list[int]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(496, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(847, part_2(self.prepared_data))
