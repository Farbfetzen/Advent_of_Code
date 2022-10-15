from unittest import TestCase

from src.util.load_data import load_data
from src.year2021.day21 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2021, 21)


@sample
class Test2021Day21Samples(TestCase):

    prepared_data: tuple[int, int]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(739785, part_1(*self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(444356092776315, part_2(*self.prepared_data))


class Test2021Day21(TestCase):

    prepared_data: tuple[int, int]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(752247, part_1(*self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(221109915584112, part_2(*self.prepared_data))
