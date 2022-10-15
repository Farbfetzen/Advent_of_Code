from unittest import TestCase

from src.util.load_data import load_data
from src.year2021.day11 import Octopuses, prepare_data
from test.decorators import sample


data = load_data(2021, 11)


@sample
class Test2021Day11Samples(TestCase):

    solution: Octopuses

    @classmethod
    def setUpClass(cls) -> None:
        prepared_data = prepare_data(data.samples[0])
        cls.solution = Octopuses(prepared_data)

    def test_part_1(self) -> None:
        self.assertEqual(1656, self.solution.flashes_after_100_steps)

    def test_part_2(self) -> None:
        self.assertEqual(195, self.solution.steps)


class Test2021Day11(TestCase):

    solution: Octopuses

    @classmethod
    def setUpClass(cls) -> None:
        prepared_data = prepare_data(data.input)
        cls.solution = Octopuses(prepared_data)

    def test_part_1(self) -> None:
        self.assertEqual(1721, self.solution.flashes_after_100_steps)

    def test_part_2(self) -> None:
        self.assertEqual(298, self.solution.steps)
