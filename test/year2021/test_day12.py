from collections import defaultdict
from unittest import TestCase

from parameterized import parameterized

from src.util.load_data import load_data
from src.year2021.day12 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2021, 12)


@sample
class Test2021Day12Samples(TestCase):

    prepared_data: list[defaultdict[str, list]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = [prepare_data(ds) for ds in data.samples]

    @parameterized.expand(((0, 10), (1, 19), (2, 226)))
    def test_part_1_samples(self, sample_index, expected):
        self.assertEqual(expected, part_1(self.prepared_data[sample_index]))

    @parameterized.expand(((0, 36), (1, 103), (2, 3509)))
    def test_part_2_samples(self, sample_index, expected):
        self.assertEqual(expected, part_2(self.prepared_data[sample_index]))


class Test2021Day12(TestCase):

    prepared_data: defaultdict[str, list]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self):
        self.assertEqual(5920, part_1(self.prepared_data))

    def test_part_2(self):
        self.assertEqual(155477, part_2(self.prepared_data))
