from unittest import TestCase

from parameterized import parameterized

from src.util.load_data import load_data
from src.year2019.day07 import build_amps, part_1, part_2, prepare_data, test_phase_setting
from test.decorators import sample


data = load_data(2019, 7)


@sample
class Test2019Day07Samples(TestCase):

    prepared_data: list[list[int]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = [prepare_data(s) for s in data.samples]

    @parameterized.expand((
            (0, False, (4, 3, 2, 1, 0), 43210),
            (1, False, (0, 1, 2, 3, 4), 54321),
            (2, False, (1, 0, 4, 3, 2), 65210),
            (3, True, (9, 8, 7, 6, 5), 139629729),
            (4, True, (9, 7, 8, 5, 6), 18216)
    ))
    def test_part_1(self, sample_index, feedback_mode, phases, expected) -> None:
        self.assertEqual(
            expected,
            test_phase_setting(build_amps(self.prepared_data[sample_index], feedback_mode), phases)
        )


class Test2019Day07(TestCase):

    prepared_data: list[int]

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(21000, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        self.assertEqual(61379886, part_2(self.prepared_data))
