from unittest import TestCase

from src.util.load_data import load_data
from src.year2021.day04 import play, prepare_data
from test.decorators import sample


data = load_data(2021, 4)


@sample
class Test2021Day04Samples(TestCase):

    solution_1: int
    solution_2: int

    @classmethod
    def setUpClass(cls) -> None:
        prepared_data = prepare_data(data.samples[0])
        cls.solution_1, cls.solution_2 = play(*prepared_data)

    def test_part_1(self) -> None:
        self.assertEqual(4512, self.solution_1)

    def test_part_2(self) -> None:
        self.assertEqual(1924, self.solution_2)


class Test2021Day04(TestCase):
    
    solution_1: int
    solution_2: int

    @classmethod
    def setUpClass(cls) -> None:
        prepared_data = prepare_data(data.input)
        cls.solution_1, cls.solution_2 = play(*prepared_data)

    def test_part_1(self) -> None:
        self.assertEqual(23177, self.solution_1)

    def test_part_2(self) -> None:
        self.assertEqual(6804, self.solution_2)
