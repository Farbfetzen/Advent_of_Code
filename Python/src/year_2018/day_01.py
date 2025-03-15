# https://adventofcode.com/2018/day/1

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2018Day01(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(prepared_input))
        self.sample_results_2.append(self.solve_2(prepared_input))

        prepared_input = self.prepare(inputs.input)
        self.result_1 = self.solve_1(prepared_input)
        self.result_2 = self.solve_2(prepared_input)

    @staticmethod
    def prepare(data: str) -> list[int]:
        return [int(line) for line in data.splitlines()]

    @staticmethod
    def solve_1(data: list[int]) -> int:
        return sum(data)

    @staticmethod
    def solve_2(data: list[int]) -> int:
        frequency = 0
        seen = set()
        while True:
            for change in data:
                if frequency in seen:
                    return frequency
                seen.add(frequency)
                frequency += change
