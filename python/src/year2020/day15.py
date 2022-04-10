# https://adventofcode.com/2020/day/15

import array

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[int]:
    return [int(x) for x in data.split(",")]


# noinspection PyUnboundLocalVariable
def play(numbers, end_turn):
    # Using an array of unsigned ints gives a small speed boost.
    memory = array.array("I", [0] * end_turn)
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


def solve(data: Data) -> Solution:
    solution = Solution()
    challenge_data = prepare_data(data.input)
    solution.part_1 = play(challenge_data, 2020)
    solution.part_2 = play(challenge_data, 30_000_000)
    return solution
