from unittest import TestCase

from src.util.load_data import load_data
from src.year2020.day20 import part_1, part_2, prepare_data, Tile
from test.decorators import sample


data = load_data(2020, 20)


@sample
class Test2020Day20Samples(TestCase):

    prepared_data: list[Tile]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(20899048083289, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(273, part_2(self.prepared_data))


class Test2020Day20(TestCase):

    prepared_data: list[Tile]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(27798062994017, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(2366, part_2(self.prepared_data))
