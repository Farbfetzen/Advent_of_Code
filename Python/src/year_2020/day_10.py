# https://adventofcode.com/2020/day/10

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2020Day10(Solution):

    def solve(self, inputs: Inputs) -> None:
        for sample in inputs.samples:
            adapters = self.prepare(sample)
            self.sample_results_1.append(self.solve_1(adapters))
            self.sample_results_2.append(self.solve_2(adapters))

        adapters = self.prepare(inputs.input)
        self.result_1 = self.solve_1(adapters)
        self.result_2 = self.solve_2(adapters)

    @staticmethod
    def prepare(data: str) -> list[int]:
        return [int(x) for x in data.splitlines()]

    @staticmethod
    def solve_1(adapters: list[int]) -> int:
        adapters.append(0)
        adapters.sort()
        adapters.append(adapters[-1] + 3)
        differences = [adapters[i + 1] - x for i, x in enumerate(adapters[:-1])]
        return differences.count(1) * (differences.count(3))

    @staticmethod
    def solve_2(adapters: list[int]) -> int:
        # Requires that part_1() ran before because the adapters must be sorted
        # and they must include 0.
        possibilities = {adapters[-1]: 1}
        for a in adapters[-2::-1]:
            possibilities[a] = sum(possibilities.get(x, 0) for x in (a + 1, a + 2, a + 3))
        return possibilities[0]
