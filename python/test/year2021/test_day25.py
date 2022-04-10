from unittest import TestCase

from src.util.load_data import load_data
from src.year2021.day25 import part_1, prepare_data
from test.decorators import sample


data = load_data(2021, 25)


class Test2021Day25(TestCase):

    @sample
    def test_part_1_sample(self) -> None:
        prepared_data = prepare_data(data.samples[0])
        self.assertEqual(58, part_1(*prepared_data))

    def test_part_1(self) -> None:
        prepared_data = prepare_data(data.input)
        self.assertEqual(532, part_1(*prepared_data))
