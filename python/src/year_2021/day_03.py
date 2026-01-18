# https://adventofcode.com/2021/day/3

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2021Day03(Solution):

    def solve(self, inputs: Inputs) -> None:
        report = inputs.samples[0].splitlines()
        self.sample_results_1.append(self.solve_1(report))
        self.sample_results_2.append(self.solve_2(report))

        report = inputs.input.splitlines()
        self.result_1 = self.solve_1(report)
        self.result_2 = self.solve_2(report)

    @staticmethod
    def count_bits(numbers: list[str]) -> list[int]:
        return [sum(int(b) for b in bits) for bits in zip(*numbers)]

    def get_rating(self, numbers: list[str], search_most_common: bool = True) -> int:
        numbers = numbers.copy()
        i = 0
        while len(numbers) > 1:
            counts = self.count_bits(numbers)
            desired_bit = counts[i] < len(numbers) / 2
            if search_most_common:
                desired_bit = not desired_bit
            numbers = [n for n in numbers if n[i] == str(int(desired_bit))]
            i += 1
        return int(numbers[0], 2)

    def solve_1(self, report: list[str]) -> int:
        sums = self.count_bits(report)
        most_common_1 = [x > len(report) / 2 for x in sums]
        gamma_rate = "".join(str(int(x)) for x in most_common_1)
        epsilon_rate = "".join(str(int(not x)) for x in most_common_1)
        return int(gamma_rate, 2) * int(epsilon_rate, 2)

    def solve_2(self, report: list[str]) -> int:
        oxygen_generator_rating = self.get_rating(report, True)
        co2_scrubber_rating = self.get_rating(report, False)
        return oxygen_generator_rating * co2_scrubber_rating
