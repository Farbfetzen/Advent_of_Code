from unittest import TestCase

from parameterized import parameterized

from src.util.load_data import load_data
from src.year2020.day18 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2020, 18)


@sample
class Test2020Day18Samples(TestCase):

    prepared_data: list[list[list[int | str]]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = [prepare_data(s) for s in data.samples]

    @parameterized.expand(((0, 71), (1, 51), (2, 26), (3, 437), (4, 12240), (5, 13632)))
    def test_part_1(self, i, expected) -> None:
        self.assertEqual(expected, part_1(self.prepared_data[i]))

    @parameterized.expand(((0, 231), (1, 51), (2, 46), (3, 1445), (4, 669060), (5, 23340)))
    def test_part_2(self, i, expected) -> None:
        self.assertEqual(expected, part_2(self.prepared_data[i]))


class Test2020Day18(TestCase):

    prepared_data: list[list[int | str]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(25190263477788, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(297139939002972, part_2(self.prepared_data))
