from unittest import TestCase

from src.util.load_data import load_data
from src.year2021.day03 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2021, 3)


@sample
class Test2021Day03Samples(TestCase):

    prepared_data: list[str]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(198, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(230, part_2(self.prepared_data))


class Test2021Day03(TestCase):
    
    prepared_data: list[str]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(693486, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(3379326, part_2(self.prepared_data))
