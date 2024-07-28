from unittest import TestCase

import numpy as np

from src.util.load_data import load_data
from src.year2019.day08 import part_1, part_2_as_string, prepare_data


data = load_data(2019, 8)


class Test2019Day08(TestCase):

    prepared_data: np.ndarray

    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.input)

    def test_part_1(self) -> None:
        self.assertEqual(2520, part_1(self.prepared_data))

    def test_part_2(self) -> None:
        expected = (
            "█    ████  ██    ██ █   █\n"
            "█    █    █  █    █ █   █\n"
            "█    ███  █       █  █ █ \n"
            "█    █    █ ██    █   █  \n"
            "█    █    █  █ █  █   █  \n"
            "████ ████  ███  ██    █  "
        )
        self.assertEqual(expected, part_2_as_string(self.prepared_data))
