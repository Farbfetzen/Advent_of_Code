# https://adventofcode.com/2020/day/5

from src.util.exceptions import ResultExpectedError
from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2020Day05(Solution):

    def solve(self, inputs: Inputs) -> None:
        self.sample_results_other["seat ids"] = [self.get_seat_id(sample) for sample in inputs.samples]

        ids = self.prepare(inputs.input)
        self.result_1 = self.solve_1(ids)
        self.result_2 = self.solve_2(ids)

    def prepare(self, data: str) -> list[int]:
        return [self.get_seat_id(p) for p in sorted(data.splitlines())]

    @staticmethod
    def get_seat_id(boarding_pass: str) -> int:
        # No need to separate rows from columns because the "row * 8" is
        # automatically handled if I treat the boarding pass as a 10 digit
        # binary number.
        binary_pass = "".join("1" if x in "BR" else "0" for x in boarding_pass)
        return int(binary_pass, 2)

    @staticmethod
    def solve_1(ids: list[int]) -> int:
        return max(ids)

    @staticmethod
    def solve_2(ids: list[int]) -> int:
        for i, id_ in enumerate(ids):
            if ids[i + 1] - id_ == 2:
                return id_ + 1
        raise ResultExpectedError
