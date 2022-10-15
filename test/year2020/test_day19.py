from unittest import TestCase

from parameterized import parameterized

from src.util.load_data import load_data
from src.year2020.day19 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2020, 19)


@sample
class Test2020Day19Samples(TestCase):

    prepared_data: list[tuple[dict[int, str | list[list[int]]], list[str]]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = [prepare_data(s) for s in data.samples]

    @parameterized.expand(((0, 2), (1, 3)))
    def test_part_1(self, i, expected) -> None:
        self.assertEqual(expected, part_1(*self.prepared_data[i]))

    def test_part_2(self) -> None:
        self.assertEqual(12, part_2(*self.prepared_data[1]))


class Test2020Day19(TestCase):

    prepared_data: tuple[dict[int, str | list[list[int]]], list[str]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(248, part_1(*self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(381, part_2(*self.prepared_data))
