from unittest import TestCase

from src.util.load_data import load_data
from src.year2021.day18 import part_1, part_2, prepare_data, SnailfishNumber
from test.decorators import sample


data = load_data(2021, 18)


@sample
class Test2021Day18Samples(TestCase):

    prepared_data: list[SnailfishNumber]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(4140, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(3993, part_2(self.prepared_data))


class Test2021Day18(TestCase):

    prepared_data: list[SnailfishNumber]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(3987, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(4500, part_2(self.prepared_data))
