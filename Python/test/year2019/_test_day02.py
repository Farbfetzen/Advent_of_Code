from unittest import TestCase

from src.util.load_data import load_data
from src.year2019.day02 import part_1, part_2, prepare_data
from src.year2019.intcode import IntcodeComputer


data = load_data(2019, 2)


class Test2019Day02(TestCase):

    prepared_data: IntcodeComputer

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(3101844, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(8478, part_2(self.prepared_data))
