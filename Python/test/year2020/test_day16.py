from typing import Any
from unittest import TestCase

from src.util.load_data import load_data
from src.year2020.day16 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2020, 16)


@sample
class Test2020Day16Samples(TestCase):

    def test_part_1(self) -> None:
        prepared_data = prepare_data(data.samples[0])
        self.assertEqual(71, part_1(prepared_data))


class Test2020Day16(TestCase):

    prepared_data: dict[str, Any]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(27802, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(279139880759, part_2(self.prepared_data))