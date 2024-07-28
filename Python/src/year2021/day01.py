# https://adventofcode.com/2021/day/1

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[int]:
    return [int(i) for i in data.splitlines()]


def part_1(depths):
    return sum(x < y for x, y in zip(depths, depths[1:]))


def part_2(depths):
    # Shortcut: I only need to compare the values that are 3 steps apart because
    # a + b + c < b + c + d can be canceled down to a < d.
    return sum(x < y for x, y in zip(depths, depths[3:]))


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
