from unittest import TestCase

from src.util.load_data import load_data
from src.year2021.day08 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2021, 8)


@sample
class Test2021Day08Samples(TestCase):

    patterns: list[list[frozenset]]
    outputs: list[list[frozenset]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.patterns, cls.outputs = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(26, part_1(self.outputs))

    def test_part_2(self) -> None:
        self.assertEqual(61229, part_2(self.patterns, self.outputs))


class Test2021Day08(TestCase):

    patterns: list[list[frozenset]]
    outputs: list[list[frozenset]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.patterns, cls.outputs = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(352, part_1(self.outputs))

    def test_part_2(self) -> None:
        self.assertEqual(936117, part_2(self.patterns, self.outputs))
