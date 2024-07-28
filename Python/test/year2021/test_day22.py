from unittest import TestCase

from parameterized import parameterized

from src.util.load_data import load_data
from src.year2021.day22 import Cuboid, part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2021, 22)


@sample
class Test2021Day22Samples(TestCase):

    prepared_data: list[list[Cuboid]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = [prepare_data(s) for s in data.samples]

    @parameterized.expand(((0, 39), (1, 590784), (2, 474140)))
    def test_part_1(self, i, expected) -> None:
        self.assertEqual(expected, part_1(self.prepared_data[i]))

    def test_part_2(self) -> None:
        self.assertEqual(2758514936282235, part_2(self.prepared_data[2]))


class Test2021Day22(TestCase):

    prepared_data: list[Cuboid]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(620241, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(1284561759639324, part_2(self.prepared_data))
