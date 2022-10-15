from unittest import TestCase

from src.util.load_data import load_data
from src.year2021.day14 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2021, 14)


@sample
class Test2021Day14Samples(TestCase):

    template: str
    rules: dict[str, str]

    @classmethod
    def setUpClass(cls) -> None:
        cls.template, cls.rules = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(1588, part_1(self.template, self.rules))

    def test_part_2(self) -> None:
        self.assertEqual(2188189693529, part_2(self.template, self.rules))


class Test2021Day14(TestCase):

    template: str
    rules: dict[str, str]

    @classmethod
    def setUpClass(cls) -> None:
        cls.template, cls.rules = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(2768, part_1(self.template, self.rules))

    def test_part_2(self) -> None:
        self.assertEqual(2914365137499, part_2(self.template, self.rules))
