# https://adventofcode.com/2021/day/6

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2021Day06(Solution):

    def solve(self, inputs: Inputs) -> None:
        fish_ages = self.prepare(inputs.samples[0])
        sample_result_1, sample_result_2 = self.simulate(fish_ages)
        self.sample_results_1.append(sample_result_1)
        self.sample_results_2.append(sample_result_2)

        fish_ages = self.prepare(inputs.input)
        self.result_1, self.result_2 = self.simulate(fish_ages)

    @staticmethod
    def prepare(data: str) -> list[int]:
        return [int(x) for x in data.split(",")]

    @staticmethod
    def simulate(fish_ages: list[int]) -> tuple[int, int]:
        count = [fish_ages.count(i) for i in range(9)]
        result_at_day_80 = 0
        for day in range(1, 256 + 1):
            zeros = count[0]
            count[:-1] = count[1:]
            count[6] += zeros
            count[8] = zeros
            if day == 80:
                result_at_day_80 = sum(count)
        return result_at_day_80, sum(count)
