from unittest import TestCase

from src.util.load_data import load_data
from src.year2021.day24 import run


data = load_data(2021, 24)


class Test2021Day24(TestCase):

    solution_1: str
    solution_2: str

    @classmethod
    def setUpClass(cls) -> None:
        cls.solution_1, cls.solution_2 = run(data.input.splitlines())

    def test_part_1(self) -> None:
        self.assertEqual("29991993698469", self.solution_1)

    def test_part_2(self) -> None:
        self.assertEqual("14691271141118", self.solution_2)
