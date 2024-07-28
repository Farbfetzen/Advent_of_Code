from unittest import TestCase

from src.util.load_data import load_data
from src.year2020.day09 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2020, 9)


@sample
class Test2020Day09Samples(TestCase):

    prepared_data: list[int]
    invalid_number: int

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])
        cls.invalid_number = part_1(cls.prepared_data, 5)

    def test_part_1(self) -> None:
        self.assertEqual(127, self.invalid_number)

    def test_part_2(self) -> None:
        self.assertEqual(62, part_2(self.prepared_data, self.invalid_number))


class Test2020Day09(TestCase):

    prepared_data: list[int]
    invalid_number: int

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)
        cls.invalid_number = part_1(cls.prepared_data, 25)

    def test_part_1(self) -> None:
        self.assertEqual(21806024, self.invalid_number)

    def test_part_2(self) -> None:
        self.assertEqual(2986195, part_2(self.prepared_data, self.invalid_number))
