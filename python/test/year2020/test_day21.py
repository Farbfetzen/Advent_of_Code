from unittest import TestCase

from src.util.load_data import load_data
from src.year2020.day21 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2020, 21)


@sample
class Test2020Day21Samples(TestCase):

    sum_safe: int
    allergen_map: dict[str, set[str]]

    @classmethod
    def setUpClass(cls) -> None:
        prepared_data = prepare_data(data.samples[0])
        cls.sum_safe, cls.allergen_map = part_1(prepared_data)

    def test_part_1(self) -> None:
        self.assertEqual(5, self.sum_safe)

    def test_part_2(self) -> None:
        self.assertEqual("mxmxvkd,sqjhc,fvjkl", part_2(self.allergen_map))


class Test2020Day21(TestCase):

    sum_safe: int
    allergen_map: dict[str, set[str]]

    @classmethod
    def setUpClass(cls) -> None:
        prepared_data = prepare_data(data.input)
        cls.sum_safe, cls.allergen_map = part_1(prepared_data)

    def test_part_1(self) -> None:
        self.assertEqual(2061, self.sum_safe)

    def test_part_2(self) -> None:
        self.assertEqual("cdqvp,dglm,zhqjs,rbpg,xvtrfz,tgmzqjz,mfqgx,rffqhl", part_2(self.allergen_map))
