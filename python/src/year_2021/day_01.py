# https://adventofcode.com/2021/day/1

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2021Day01(Solution):

    def solve(self, inputs: Inputs) -> None:
        depths = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(depths))
        self.sample_results_2.append(self.solve_2(depths))

        depths = self.prepare(inputs.input)
        self.result_1 = self.solve_1(depths)
        self.result_2 = self.solve_2(depths)

    @staticmethod
    def prepare(data: str) -> list[int]:
        return [int(i) for i in data.splitlines()]

    @staticmethod
    def solve_1(depths: list[int]) -> int:
        return sum(x < y for x, y in zip(depths, depths[1:]))

    @staticmethod
    def solve_2(depths: list[int]) -> int:
        # Shortcut: I only need to compare the values that are 3 steps apart because
        # a + b + c < b + c + d can be canceled down to a < d.
        return sum(x < y for x, y in zip(depths, depths[3:]))
