from unittest import TestCase

from src.util.load_data import load_data
from src.year2020.day14 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2020, 14)


@sample
class Test2020Day14Samples(TestCase):

    prepared_data: list[list[str]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = [prepare_data(s) for s in data.samples]

    def test_part_1(self) -> None:
        self.assertEqual(165, part_1(self.prepared_data[0]))

    def test_part_2(self) -> None:
        self.assertEqual(208, part_2(self.prepared_data[1]))


class Test2020Day14(TestCase):

    prepared_data: list[str]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(4297467072083, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(5030603328768, part_2(self.prepared_data))
