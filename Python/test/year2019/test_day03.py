from unittest import TestCase

from parameterized import parameterized

from src.util.load_data import load_data
from src.year2019.day03 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2019, 3)


@sample
class Test2019Day03Samples(TestCase):

    prepared_data: list[list[str]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = [prepare_data(s) for s in data.samples]

    @parameterized.expand(((0, 159), (1, 135)))
    def test_part_1(self, sample_index, expected) -> None:
        self.assertEqual(expected, part_1(self.prepared_data[sample_index]))

    @parameterized.expand(((0, 610), (1, 410)))
    def test_part_2(self, sample_index, expected) -> None:
        self.assertEqual(expected, part_2(self.prepared_data[sample_index]))


class Test2019Day03(TestCase):

    prepared_data: list[str]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(489, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(93654, part_2(self.prepared_data))
