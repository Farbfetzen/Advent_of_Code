from unittest import TestCase

from src.util.load_data import load_data
from src.year2020.day23 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2020, 23)


@sample
class Test2020Day23Samples(TestCase):

    prepared_data: list[int]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual("67384529", part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual("149245887792", part_2(self.prepared_data))


class Test2020Day23(TestCase):

    prepared_data: list[int]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual("24798635", part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual("12757828710", part_2(self.prepared_data))
