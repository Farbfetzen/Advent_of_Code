from unittest import TestCase

from src.util.load_data import load_data
from src.year2018.day04 import analyze_sleep_patterns, part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2018, 4)


@sample
class Test2018Day04Samples(TestCase):

    sleep_pattenrs:  dict[str, list[int]]

    @classmethod
    def setUpClass(cls) -> None:
        prepared_data = prepare_data(data.samples[0])
        cls.sleep_pattenrs = analyze_sleep_patterns(prepared_data)

    def test_part_1(self) -> None:
        self.assertEqual(240, part_1(self.sleep_pattenrs))

    def test_part_2(self) -> None:
        self.assertEqual(4455, part_2(self.sleep_pattenrs))


class Test2018Day04(TestCase):

    sleep_pattenrs:  dict[str, list[int]]

    @classmethod
    def setUpClass(cls) -> None:
        prepared_data = prepare_data(data.input)
        cls.sleep_pattenrs = analyze_sleep_patterns(prepared_data)

    def test_part_1(self) -> None:
        self.assertEqual(60438, part_1(self.sleep_pattenrs))

    def test_part_2(self) -> None:
        self.assertEqual(47989, part_2(self.sleep_pattenrs))
