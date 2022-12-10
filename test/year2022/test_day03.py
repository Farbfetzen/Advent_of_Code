from unittest import TestCase

from src.util.load_data import load_data
from src.year2022.day03 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2022, 3)


@sample
class Test2022Day03Samples(TestCase):

    prepared_data: list[str]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(157, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(70, part_2(self.prepared_data))


class Test2022Day03(TestCase):

    prepared_data: list[str]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(7766, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(2415, part_2(self.prepared_data))
