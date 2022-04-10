from unittest import TestCase

from src.util.load_data import load_data
from src.year2021.day20 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2021, 20)


@sample
class Test2021Day20Samples(TestCase):

    prepared_data: tuple[list[int], list[list[int]]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(35, part_1(*self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(3351, part_2(*self.prepared_data))


class Test2021Day20(TestCase):

    prepared_data: tuple[list[int], list[list[int]]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(5081, part_1(*self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(15088, part_2(*self.prepared_data))
