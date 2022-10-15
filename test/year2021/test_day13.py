from unittest import TestCase

from src.util.load_data import load_data
from src.util.types import Point2
from src.year2021.day13 import Fold, part_1, part_2, prepare_data
from test.decorators import sample


data = load_data(2021, 13)


@sample
class Test2021Day13Samples(TestCase):

    folds: list[Fold]
    points: set[Point2]

    @classmethod
    def setUpClass(cls) -> None:
        cls.points, cls.folds = prepare_data(data.samples[0])

    def test_part_1(self) -> None:
        self.assertEqual(17, part_1(self.points, self.folds))

    def test_part_2(self) -> None:
        expected = (
            "█████\n"
            "█   █\n"
            "█   █\n"
            "█   █\n"
            "█████"
        )
        self.assertEqual(
            expected,
            part_2(self.points, self.folds)
        )


class Test2021Day13(TestCase):

    folds: list[Fold]
    points: set[Point2]

    @classmethod
    def setUpClass(cls) -> None:
        cls.points, cls.folds = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(807, part_1(self.points, self.folds))

    def test_part_2(self) -> None:
        expected = (
            "█     ██  █  █ ████  ██  █  █ ████   ██\n"
            "█    █  █ █  █ █    █  █ █  █ █       █\n"
            "█    █    ████ ███  █    █  █ ███     █\n"
            "█    █ ██ █  █ █    █ ██ █  █ █       █\n"
            "█    █  █ █  █ █    █  █ █  █ █    █  █\n"
            "████  ███ █  █ ████  ███  ██  ████  ██ "
        )
        self.assertEqual(expected, part_2(self.points, self.folds))
