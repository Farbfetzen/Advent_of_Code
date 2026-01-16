# https://adventofcode.com/2022/day/1

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2022Day01(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(prepared_input))
        self.sample_results_2.append(self.solve_2(prepared_input))

        prepared_input = self.prepare(inputs.input)
        self.result_1 = self.solve_1(prepared_input)
        self.result_2 = self.solve_2(prepared_input)

    @staticmethod
    def prepare(data: str) -> list[list[int]]:
        return [[int(x) for x in line.split()] for line in data.split("\n\n")]

    @staticmethod
    def solve_1(data: list[list[int]]) -> int:
        return max(sum(x) for x in data)

    @staticmethod
    def solve_2(data: list[list[int]]) -> int:
        return sum(sorted((sum(x) for x in data), reverse=True)[:3])
