# https://adventofcode.com/2020/day/25

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2020Day25(Solution):

    def solve(self, inputs: Inputs) -> None:
        public_keys = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(public_keys))

        public_keys = self.prepare(inputs.input)
        self.result_1 = self.solve_1(public_keys)

        # No part 2 on the 25th.

    @staticmethod
    def prepare(data: str) -> list[int]:
        return [int(x) for x in data.splitlines()]

    @staticmethod
    def solve_1(public_keys: list[int]) -> int:
        value = 1
        found = 0
        loop_sizes = [0, 0]
        i = 0
        while True:
            i += 1
            value = (value * 7) % 20201227
            if value in public_keys:
                loop_sizes[public_keys.index(value)] = i
                found += 1
            if found == 2:
                break

        loop_size = min(loop_sizes)  # Save time by using the smaller loop size.
        public_key = public_keys[loop_sizes.index(max(loop_sizes))]
        value = 1
        for _ in range(loop_size):
            value = (value * public_key) % 20201227
        return value
