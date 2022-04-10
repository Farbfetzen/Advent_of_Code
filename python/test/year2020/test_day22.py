from collections import deque
from unittest import TestCase

from src.util.load_data import load_data
from src.year2020.day22 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2020, 22)


@sample
class Test2020Day22Samples(TestCase):

    prepared_data: list[deque[int]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(306, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(291, part_2(self.prepared_data))


class Test2020Day22(TestCase):

    prepared_data: list[deque[int]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(30138, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(31587, part_2(self.prepared_data))
