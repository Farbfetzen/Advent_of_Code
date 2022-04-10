from unittest import TestCase

from src.util.load_data import load_data
from src.year2021.day17 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2021, 17)


@sample
class Test2021Day17Samples(TestCase):

    prepared_data: list[int]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(45, part_1(self.prepared_data[2]))

    def test_part_2(self) -> None:
        self.assertEqual(112, part_2(*self.prepared_data))


class Test2021Day17(TestCase):

    prepared_data: list[int]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(17766, part_1(self.prepared_data[2]))

    def test_part_2(self) -> None:
        self.assertEqual(1733, part_2(*self.prepared_data))
