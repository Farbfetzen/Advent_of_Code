from unittest import TestCase

from src.util.load_data import load_data
from src.year2021.day06 import prepare_data, simulate
from test.decorators import sample


data = load_data(2021, 6)


@sample
class Test2021Day06Samples(TestCase):

    solution_1: int
    solution_2: int

    @classmethod
    def setUpClass(cls) -> None:
        prepared_data = prepare_data(data.samples[0])
        cls.solution_1, cls.solution_2 = simulate(prepared_data)

    def test_part_1(self) -> None:
        self.assertEqual(5934, self.solution_1)

    def test_part_2(self) -> None:
        self.assertEqual(26984457539, self.solution_2)


class Test2021Day06(TestCase):

    solution_1: int
    solution_2: int

    @classmethod
    def setUpClass(cls) -> None:
        prepared_data = prepare_data(data.input)
        cls.solution_1, cls.solution_2 = simulate(prepared_data)

    def test_part_1(self) -> None:
        self.assertEqual(372300, self.solution_1)

    def test_part_2(self) -> None:
        self.assertEqual(1675781200288, self.solution_2)
