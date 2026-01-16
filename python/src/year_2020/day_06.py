# https://adventofcode.com/2020/day/6

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2020Day06(Solution):

    def solve(self, inputs: Inputs) -> None:
        groups = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(groups))
        self.sample_results_2.append(self.solve_2(groups))

        groups = self.prepare(inputs.input)
        self.result_1 = self.solve_1(groups)
        self.result_2 = self.solve_2(groups)

    @staticmethod
    def prepare(data: str) -> list[list[set[str]]]:
        return [[set(person) for person in group.splitlines()] for group in data.split("\n\n")]

    @staticmethod
    def solve_1(groups: list[list[set[str]]]) -> int:
        return sum(len(set.union(*group)) for group in groups)

    @staticmethod
    def solve_2(groups: list[list[set[str]]]) -> int:
        return sum(len(set.intersection(*group)) for group in groups)
