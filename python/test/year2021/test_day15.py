from unittest import TestCase

from src.util.load_data import load_data
from src.year2021.day15 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2021, 15)


@sample
class Test2021Day15Samples(TestCase):

    prepared_data: list[list[int]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(40, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(315, part_2(self.prepared_data))


class Test2021Day15(TestCase):

    prepared_data: list[list[int]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(717, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(2993, part_2(self.prepared_data))
