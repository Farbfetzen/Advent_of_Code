from unittest import TestCase

from src.util.load_data import load_data
from src.year2020.day03 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2020, 3)


@sample
class Test2020Day03Samples(TestCase):

    def test_part_1(self) -> None:
        prepared_data = prepare_data(data.samples[0])
        self.assertEqual(7, part_1(prepared_data))


class Test2020Day03(TestCase):

    prepared_data: list[list[bool]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(211, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(3584591857, part_2(self.prepared_data))
