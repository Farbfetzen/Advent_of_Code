from unittest import TestCase

from src.util.load_data import load_data
from src.year2021.day19 import part_1, part_2, prepare_data, Scanner
from test.decorators import sample


data = load_data(2021, 19)


@sample
class Test2021Day19Samples(TestCase):

    prepared_data: list[Scanner]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(79, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(3621, part_2(self.prepared_data))


class Test2021Day19(TestCase):

    prepared_data: list[Scanner]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(451, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(13184, part_2(self.prepared_data))
