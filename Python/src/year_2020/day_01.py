# https://adventofcode.com/2020/day/1

from src.util.exceptions import ResultExpectedError
from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2020Day01(Solution):

    def solve(self, inputs: Inputs) -> None:
        expenses = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(expenses))
        self.sample_results_2.append(self.solve_2(expenses))

        expenses = self.prepare(inputs.input)
        self.result_1 = self.solve_1(expenses)
        self.result_2 = self.solve_2(expenses)

    @staticmethod
    def prepare(data: str) -> list[int]:
        return [int(i) for i in data.splitlines()]

    @staticmethod
    def solve_1(expenses: list[int]) -> int:
        # Add numbers to the set after checking to avoid possible error
        # if the data contains 1010.
        seen = set()
        for x in expenses:
            y = 2020 - x
            if y in seen:
                return x * y
            seen.add(x)
        raise ResultExpectedError

    @staticmethod
    def solve_2(expenses: list[int]) -> int:
        seen = set()
        for i, x in enumerate(expenses):
            for j, y in enumerate(expenses[(i + 1) :]):
                z = 2020 - x - y
                if z in seen:
                    return x * y * z
                seen.add(x)
                seen.add(y)
        raise ResultExpectedError
