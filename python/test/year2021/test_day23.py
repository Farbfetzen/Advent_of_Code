from unittest import TestCase

from src.util.load_data import load_data
from src.year2021.day23 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2021, 23)


@sample
class Test2021Day23Samples(TestCase):

    def test_part_1(self) -> None:
        prepared_data = prepare_data(data.samples[0], False)
        self.assertEqual(12521, part_1(*prepared_data))

    def test_part_2(self) -> None:
        prepared_data = prepare_data(data.samples[0], True)
        self.assertEqual(44169, part_2(*prepared_data))


class Test2021Day23(TestCase):

    def test_part_1(self) -> None:
        prepared_data = prepare_data(data.input, False)
        self.assertEqual(12240, part_1(*prepared_data))

    def test_part_2(self) -> None:
        prepared_data = prepare_data(data.input, True)
        self.assertEqual(44618, part_2(*prepared_data))
