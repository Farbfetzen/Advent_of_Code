from unittest import TestCase

from src.util.load_data import load_data
from src.year2018.day03 import part_1_and_2, prepare_data


data = load_data(2018, 3)


class Test2018Day03(TestCase):

    solution_part_1: int
    solution_part_2: int

    @classmethod
    def setUpClass(cls) -> None:
        prepared_data = prepare_data(data.input)
        cls.solution_part_1, cls.solution_part_2 = part_1_and_2(prepared_data)

    def test_part_1(self) -> None:
        self.assertEqual(104126, self.solution_part_1)

    def test_part_2(self) -> None:
        self.assertEqual(695, self.solution_part_2)
