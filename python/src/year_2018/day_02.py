# https://adventofcode.com/2018/day/2

import collections

from src.util.exceptions import ResultExpectedError
from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2018Day02(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = inputs.samples[0].splitlines()
        self.sample_results_1.append(self.solve_1(prepared_input))
        prepared_input = inputs.samples[1].splitlines()
        self.sample_results_2.append(self.solve_2(prepared_input))

        prepared_input = inputs.input.splitlines()
        self.result_1 = self.solve_1(prepared_input)
        self.result_2 = self.solve_2(prepared_input)

    @staticmethod
    def solve_1(data: list[str]) -> int:
        sum_2 = 0
        sum_3 = 0
        for id_ in data:
            counter = collections.Counter(id_)
            sum_2 += 2 in counter.values()
            sum_3 += 3 in counter.values()
        return sum_2 * sum_3

    @staticmethod
    def find_ids_differing_by_1(data: list[str]) -> tuple[str, str]:
        for id_1 in data:
            for id_2 in data:
                count_differences = 0
                for a, b in zip(id_1, id_2):
                    count_differences += a != b
                if count_differences == 1:
                    return id_1, id_2
        raise ResultExpectedError

    def solve_2(self, data: list[str]) -> str:
        id_1, id_2 = self.find_ids_differing_by_1(data)
        for x in enumerate(zip(id_1, id_2)):
            i = x[0]
            a, b = x[1]
            if a != b:
                return id_1[:i] + id_1[i + 1 :]
        raise ResultExpectedError
