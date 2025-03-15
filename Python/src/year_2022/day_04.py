# https://adventofcode.com/2022/day/4

from re import findall

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2022Day04(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(prepared_input))
        self.sample_results_2.append(self.solve_2(prepared_input))

        prepared_input = self.prepare(inputs.input)
        self.result_1 = self.solve_1(prepared_input)
        self.result_2 = self.solve_2(prepared_input)

    @staticmethod
    def prepare(data: str) -> list[list[int]]:
        return [[int(x) for x in findall(r"(\d+)", line)] for line in data.splitlines()]

    @staticmethod
    def solve_1(assignments: list[list[int]]) -> int:
        n_containing = 0
        for min_1, max_1, min_2, max_2 in assignments:
            n_containing += min_1 <= min_2 and max_1 >= max_2 or min_1 >= min_2 and max_1 <= max_2
        return n_containing

    @staticmethod
    def solve_2(assignments: list[list[int]]) -> int:
        n_overlapping = 0
        for min_1, max_1, min_2, max_2 in assignments:
            n_overlapping += min_1 <= max_2 and min_2 <= max_1
        return n_overlapping
