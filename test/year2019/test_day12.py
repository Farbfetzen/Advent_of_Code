from unittest import TestCase

from src.util.load_data import load_data
from src.year2019.day12 import prepare_data, simulate
from test.decorators import sample


data = load_data(2019, 12)


@sample
class Test2019Day12Samples(TestCase):

    prepared_data_0: list[list[int]]
    prepared_data_1: list[list[int]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data_0 = prepare_data(data.samples[0])
        cls.prepared_data_1 = prepare_data(data.samples[1])

    def test_sample_0(self) -> None:
        energy, period = simulate(self.prepared_data_0, 10)
        self.assertEqual(179, energy)
        self.assertEqual(2772, period)

    def test_sample_1(self) -> None:
        energy, period = simulate(self.prepared_data_1, 100)
        self.assertEqual(1940, energy)
        self.assertEqual(4686774924, period)


class Test2019Day12(TestCase):

    prepared_data: list[list[int]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_both(self) -> None:
        energy, period = simulate(self.prepared_data, 1000)
        self.assertEqual(8742, energy)
        self.assertEqual(325433763467176, period)
