from unittest import TestCase

from parameterized import parameterized

from src.util.load_data import load_data
from src.year2021.day16 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2021, 16)


@sample
class Test2021Day16Samples(TestCase):

    prepared_data: list[str]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = [prepare_data(s) for s in data.samples]

    @parameterized.expand(((0, 16), (1, 12), (2, 23), (3, 31)))
    def test_part_1(self, i, expected) -> None:
        self.assertEqual(expected, part_1(self.prepared_data[i]))

    @parameterized.expand(((4, 3), (5, 54), (6, 7), (7, 9), (8, 1), (9, 0), (10, 0), (11, 1)))
    def test_part_2(self, i, expected) -> None:
        self.assertEqual(expected, part_2(self.prepared_data[i]))


class Test2021Day16(TestCase):

    prepared_data: str

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(940, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(13476220616073, part_2(self.prepared_data))
