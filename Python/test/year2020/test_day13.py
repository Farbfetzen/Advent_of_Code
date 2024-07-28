from unittest import TestCase

from src.util.load_data import load_data
from src.year2020.day13 import part_1, part_2, part_2_without_crt, prepare_data
from test.decorators import sample


data = load_data(2020, 13)


@sample
class Test2020Day13Samples(TestCase):

    prepared_data: list[str]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(295, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(1068781, part_2(self.prepared_data))

    def test_part_2_without_crt(self):
        self.assertEqual(1068781, part_2_without_crt(self.prepared_data))


class Test2020Day13(TestCase):

    prepared_data: list[str]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(3882, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(867295486378319, part_2(self.prepared_data))

    def test_part_2_without_crt(self) -> None:
        self.assertEqual(867295486378319, part_2_without_crt(self.prepared_data))
