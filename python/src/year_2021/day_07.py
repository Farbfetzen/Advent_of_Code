# https://adventofcode.com/2021/day/7

from math import ceil, floor
from statistics import mean, median

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2021Day07(Solution):

    def solve(self, inputs: Inputs) -> None:
        positions = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(positions))
        self.sample_results_2.append(self.solve_2(positions))

        positions = self.prepare(inputs.input)
        self.result_1 = self.solve_1(positions)
        self.result_2 = self.solve_2(positions)

    @staticmethod
    def prepare(data: str) -> list[int]:
        return [int(x) for x in data.split(",")]

    @staticmethod
    def solve_1(positions: list[int]) -> int:
        best_position = int(median(positions))
        return sum(abs(pos - best_position) for pos in positions)

    @staticmethod
    def solve_2(positions: list[int]) -> int:
        mean_position = mean(positions)
        # Because the positions have to be ints I need to check both around the mean.
        best_positions = (floor(mean_position), ceil(mean_position))
        fuel_requirements = [0, 0]
        for i, bp in enumerate(best_positions):
            fuel = 0
            for pos in positions:
                steps = abs(pos - bp)
                fuel += steps * (steps + 1) // 2
            fuel_requirements[i] = fuel
        return int(min(fuel_requirements))
