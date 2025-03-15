# https://adventofcode.com/2022/day/1

from src.util.types import Inputs, Solution


class Solution2022Day1(Solution):

    def solve(self, inputs: Inputs) -> None:
        sample_data = self.prepare(inputs.samples[0])
        self.samples_1.append(self.solve_1(sample_data))
        self.samples_2.append(self.solve_2(sample_data))

        puzzle_data = self.prepare(inputs.input)
        self.result_1 = self.solve_1(puzzle_data)
        self.result_2 = self.solve_2(puzzle_data)

    @staticmethod
    def prepare(data: str) -> list[list[int]]:
        return [[int(x) for x in line.split()] for line in data.split("\n\n")]

    @staticmethod
    def solve_1(data: list[list[int]]) -> int:
        return max(sum(x) for x in data)

    @staticmethod
    def solve_2(data: list[list[int]]) -> int:
        return sum(sorted((sum(x) for x in data), reverse=True)[:3])
