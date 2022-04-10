from unittest import TestCase

from parameterized import parameterized

from src.util.load_data import load_data
from src.year2020.day07 import Bag, part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2020, 7)


@sample
class Test2020Day07Samples(TestCase):

    prepared_data: list[dict[str, list[Bag]]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = [prepare_data(s) for s in data.samples]

    def test_part_1(self) -> None:
        self.assertEqual(4, part_1(self.prepared_data[0]))

    @parameterized.expand(((0, 32), (1, 126)))
    def test_part_2(self, i, expected) -> None:
        self.assertEqual(expected, part_2(self.prepared_data[i]))


class Test2020Day07(TestCase):

    prepared_data: dict[str, list[Bag]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(348, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(18885, part_2(self.prepared_data))
