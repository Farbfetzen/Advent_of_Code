from unittest import TestCase

from parameterized import parameterized

from src.util.load_data import load_data
from src.year2019.day16 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2019, 16)


@sample
class Test2019Day16Samples(TestCase):

    prepared_data: list[list[int]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = [prepare_data(ds) for ds in data.samples]

    @parameterized.expand(((0, "24176176"), (1, "73745418"), (2, "52432133")))
    def test_part_1(self, sample_index, expected) -> None:
        self.assertEqual(expected, part_1(self.prepared_data[sample_index]))

    @parameterized.expand(((3, "84462026"), (4, "78725270"), (5, "53553731")))
    def test_part_2(self, sample_index, expected) -> None:
        self.assertEqual(expected, part_2(self.prepared_data[sample_index]))


class Test2019Day16(TestCase):

    prepared_data: list[int]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual("74608727", part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual("57920757", part_2(self.prepared_data))
