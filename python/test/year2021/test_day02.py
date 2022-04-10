from unittest import TestCase

from src.util.load_data import load_data
from src.year2021.day02 import follow_course, part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2021, 2)


@sample
class Test2021Day02Samples(TestCase):

    horiz_pos: int
    depth: int
    aim: int

    @classmethod
    def setUpClass(cls) -> None:
        prepared_data = prepare_data(data.samples[0])
        cls.horiz_pos, cls.depth, cls.aim = follow_course(prepared_data)

    def test_part_1(self) -> None:
        self.assertEqual(150, part_1(self.horiz_pos, self.aim))

    def test_part_2(self) -> None:
        self.assertEqual(900, part_2(self.horiz_pos, self.depth))


class Test2021Day02(TestCase):

    horiz_pos: int
    depth: int
    aim: int

    @classmethod
    def setUpClass(cls) -> None:
        prepared_data = prepare_data(data.input)
        cls.horiz_pos, cls.depth, cls.aim = follow_course(prepared_data)

    def test_part_1(self) -> None:
        self.assertEqual(2073315, part_1(self.horiz_pos, self.aim))

    def test_part_2(self) -> None:
        self.assertEqual(1840311528, part_2(self.horiz_pos, self.depth))
