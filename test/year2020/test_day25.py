from unittest import TestCase

from src.util.load_data import load_data
from src.year2020.day25 import part_1, prepare_data
from test.decorators import sample


data = load_data(2020, 25)


class Test2020Day25(TestCase):

    @sample
    def test_part_1_sample(self) -> None:
        prepared_data = prepare_data(data.samples[0])
        self.assertEqual(14897079, part_1(prepared_data))

    def test_part_1(self) -> None:
        prepared_data = prepare_data(data.input)
        self.assertEqual(16902792, part_1(prepared_data))
