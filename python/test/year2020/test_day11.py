from unittest import TestCase

import numpy

from src.util.load_data import load_data
from src.year2020.day11 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2020, 11)


@sample
class Test2020Day11Samples(TestCase):

    prepared_data: numpy.ndarray

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(37, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(26, part_2(self.prepared_data))


class Test2020Day11(TestCase):

    prepared_data: numpy.ndarray

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(2299, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(2047, part_2(self.prepared_data))
