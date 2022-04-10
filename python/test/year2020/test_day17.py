from unittest import TestCase

from src.util.load_data import load_data
from src.year2020.day17 import prepare_data, run_reactor
from test.decorators import sample


data = load_data(2020, 17)


@sample
class Test2020Day17Samples(TestCase):

    prepared_data: list[str]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(112, run_reactor(self.prepared_data, 3))

    def test_part_2(self) -> None:
        self.assertEqual(848, run_reactor(self.prepared_data, 4))


class Test2020Day17(TestCase):

    prepared_data: list[str]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(232, run_reactor(self.prepared_data, 3))

    def test_part_2(self) -> None:
        self.assertEqual(1620, run_reactor(self.prepared_data, 4))
