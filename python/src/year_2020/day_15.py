# https://adventofcode.com/2020/day/15

import array

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2020Day15(Solution):

    def solve(self, inputs: Inputs) -> None:
        numbers = self.prepare(inputs.input)
        self.result_1 = self.play(numbers, 2020)
        self.result_2 = self.play(numbers, 30_000_000)

    @staticmethod
    def prepare(data: str) -> list[int]:
        return [int(x) for x in data.split(",")]

    @staticmethod
    def play(numbers: list[int], end_turn: int) -> int:
        # Using an array of unsigned ints gives a small speed boost.
        memory = array.array("I", [0] * end_turn)
        turn = 0
        last_seen = 0
        last_num = 0
        for turn, last_num in enumerate(numbers, start=1):
            last_seen = memory[last_num]
            memory[last_num] = turn
        for turn in range(turn + 1, end_turn + 1):
            if last_seen > 0:
                last_num = turn - last_seen - 1
            else:
                last_num = 0
            last_seen = memory[last_num]
            memory[last_num] = turn
        return last_num
