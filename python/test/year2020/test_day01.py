from unittest import TestCase

from src.util.load_data import load_data
from src.year2020.day01 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2020, 1)


@sample
class Test2020Day01Samples(TestCase):

    prepared_data: list[int]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(514579, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(241861950, part_2(self.prepared_data))


class Test2020Day01(TestCase):

    prepared_data: list[int]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(436404, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(274879808, part_2(self.prepared_data))
