from unittest import TestCase

from parameterized import parameterized

from src.util.load_data import load_data
from src.year2020.day10 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2020, 10)


@sample
class Test2020Day10Samples(TestCase):

    prepared_data: list[list[int]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = [prepare_data(s) for s in data.samples]

    @parameterized.expand(((0, 35), (1, 220)))
    def test_part_1(self, i, expected) -> None:
        self.assertEqual(expected, part_1(self.prepared_data[i]))

    @parameterized.expand(((0, 8), (1, 19208)))
    def test_part_2(self, i, expected) -> None:
        self.assertEqual(expected, part_2(self.prepared_data[i]))


class Test2020Day10(TestCase):

    prepared_data: list[int]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(2760, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(13816758796288, part_2(self.prepared_data))
