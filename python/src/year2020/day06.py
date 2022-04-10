# https://adventofcode.com/2020/day/6

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[list[set[str]]]:
    return [[set(person) for person in group.splitlines()] for group in data.split("\n\n")]


def part_1(groups):
    return sum(len(set.union(*group)) for group in groups)


def part_2(groups):
    return sum(len(set.intersection(*group)) for group in groups)


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
