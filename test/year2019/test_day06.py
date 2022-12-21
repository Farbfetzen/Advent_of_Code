from unittest import TestCase

from src.util.load_data import load_data
from src.year2019.day06 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2019, 6)


@sample
class Test2019Day06Samples(TestCase):

    prepared_data: list[dict[str, str]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = [prepare_data(s) for s in data.samples]

    def test_part_1(self) -> None:
        self.assertEqual(42, part_1(self.prepared_data[0]))

    def test_part_2(self) -> None:
        self.assertEqual(4, part_2(self.prepared_data[1]))


class Test2019Day06(TestCase):

    prepared_data: dict[str, str]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(253104, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(499, part_2(self.prepared_data))
