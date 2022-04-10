from unittest import TestCase

from src.util.load_data import load_data
from src.year2021.day10 import get_scores, prepare_data
from test.decorators import sample


data = load_data(2021, 10)


@sample
class Test2021Day10Samples(TestCase):

    solution_1: int
    solution_2: int

    @classmethod
    def setUpClass(cls) -> None:
        prepared_data = prepare_data(data.samples[0])
        cls.solution_1, cls.solution_2 = get_scores(prepared_data)

    def test_part_1(self) -> None:
        self.assertEqual(26397, self.solution_1)

    def test_part_2(self) -> None:
        self.assertEqual(288957, self.solution_2)


class Test2021Day10(TestCase):

    solution_1: int
    solution_2: int

    @classmethod
    def setUpClass(cls) -> None:
        prepared_data = prepare_data(data.input)
        cls.solution_1, cls.solution_2 = get_scores(prepared_data)

    def test_part_1(self) -> None:
        self.assertEqual(362271, self.solution_1)

    def test_part_2(self) -> None:
        self.assertEqual(1698395182, self.solution_2)
