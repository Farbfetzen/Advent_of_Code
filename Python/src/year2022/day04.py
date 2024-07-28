# https://adventofcode.com/2022/day/4

from re import findall

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[list[int]]:
    return [[int(x) for x in findall(r"(\d+)", line)] for line in data.splitlines()]


def part_1(assignments: list[list[int]]) -> int:
    n_containing = 0
    for min_1, max_1, min_2, max_2 in assignments:
        n_containing += min_1 <= min_2 and max_1 >= max_2 or min_1 >= min_2 and max_1 <= max_2
    return n_containing


def part_2(assignments: list[list[int]]) -> int:
    n_overlapping = 0
    for min_1, max_1, min_2, max_2 in assignments:
        n_overlapping += min_1 <= max_2 and min_2 <= max_1
    return n_overlapping


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
