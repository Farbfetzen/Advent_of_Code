from unittest import TestCase

from src.util.load_data import load_data
from src.year2020.day08 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2020, 8)


@sample
class Test2020Day08Samples(TestCase):

    prepared_data: list[tuple[str, int]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(5, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(8, part_2(self.prepared_data))


class Test2020Day08(TestCase):

    prepared_data: list[tuple[str, int]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(1262, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(1643, part_2(self.prepared_data))
