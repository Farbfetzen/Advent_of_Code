# https://adventofcode.com/2019/day/1

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2019Day01(Solution):

    def solve(self, inputs: Inputs) -> None:
        masses = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(masses))
        self.sample_results_2.append(self.solve_2(masses))

        masses = self.prepare(inputs.input)
        self.result_1 = self.solve_1(masses)
        self.result_2 = self.solve_2(masses)

    @staticmethod
    def prepare(data: str) -> list[int]:
        return [int(i) for i in data.splitlines()]

    @staticmethod
    def calculate_fuel(mass: int) -> int:
        return max(mass // 3 - 2, 0)

    def solve_1(self, masses: list[int]) -> int:
        return sum(self.calculate_fuel(m) for m in masses)

    def solve_2(self, masses: list[int]) -> int:
        total = 0
        for m in masses:
            additional_fuel = self.calculate_fuel(m)
            while additional_fuel > 0:
                total += additional_fuel
                additional_fuel = self.calculate_fuel(additional_fuel)
        return total
