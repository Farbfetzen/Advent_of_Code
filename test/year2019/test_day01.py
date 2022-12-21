from unittest import TestCase

from src.util.load_data import load_data
from src.year2019.day01 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2019, 1)


@sample
class Test2019Day01Samples(TestCase):

    prepared_data: list[int]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(34241, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(51316, part_2(self.prepared_data))


class Test2019Day01(TestCase):

    prepared_data: list[int]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(3223398, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(4832253, part_2(self.prepared_data))
