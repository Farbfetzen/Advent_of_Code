from unittest import TestCase

from src.util.load_data import load_data
from src.util.types import Point2
from src.year2021.day09 import part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2021, 9)


@sample
class Test2021Day09Samples(TestCase):

    heightmap: tuple[tuple[int, ...], ...]
    low_points: list[Point2]

    @classmethod
    def setUpClass(cls) -> None:
        cls.heightmap, cls.low_points = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(15, part_1(self.heightmap, self.low_points))

    def test_part_2(self) -> None:
        self.assertEqual(1134, part_2(self.heightmap, self.low_points))


class Test2021Day09(TestCase):

    heightmap: tuple[tuple[int, ...], ...]
    low_points: list[Point2]

    @classmethod
    def setUpClass(cls) -> None:
        cls.heightmap, cls.low_points = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(554, part_1(self.heightmap, self.low_points))

    def test_part_2(self) -> None:
        self.assertEqual(1017792, part_2(self.heightmap, self.low_points))
