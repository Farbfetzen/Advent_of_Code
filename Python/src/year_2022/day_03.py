# https://adventofcode.com/2022/day/3

from string import ascii_letters

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2022Day03(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = inputs.samples[0].splitlines()
        self.sample_results_1.append(self.solve_1(prepared_input))
        self.sample_results_2.append(self.solve_2(prepared_input))

        prepared_input = inputs.input.splitlines()
        self.result_1 = self.solve_1(prepared_input)
        self.result_2 = self.solve_2(prepared_input)

    @staticmethod
    def sum_priorities(items: list[str]) -> int:
        return sum(ascii_letters.index(item) + 1 for item in items)

    def solve_1(self, data: list[str]) -> int:
        common_items = []
        for line in data:
            middle = len(line) // 2
            left = set(line[:middle])
            right = set(line[middle:])
            common_items.append(left.intersection(right).pop())
        return self.sum_priorities(common_items)

    def solve_2(self, data: list[str]) -> int:
        common_items = []
        for i in range(0, len(data), 3):
            sets = [set(rucksack) for rucksack in data[i:i + 3]]
            common_items.append(set.intersection(*sets).pop())
        return self.sum_priorities(common_items)
