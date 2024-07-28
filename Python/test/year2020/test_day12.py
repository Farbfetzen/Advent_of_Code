from unittest import TestCase

from src.util.load_data import load_data
from src.year2020.day12 import navigate, prepare_data
from test.decorators import sample


data = load_data(2020, 12)


@sample
class Test2020Day12Samples(TestCase):

    prepared_data: list[str]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(25, navigate(self.prepared_data, part=1))

    def test_part_2(self) -> None:
        self.assertEqual(286, navigate(self.prepared_data, part=2))


class Test2020Day12(TestCase):

    prepared_data: list[str]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(362, navigate(self.prepared_data, part=1))

    def test_part_2(self) -> None:
        self.assertEqual(29895, navigate(self.prepared_data, part=2))
