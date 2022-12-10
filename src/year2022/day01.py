# https://adventofcode.com/2022/day/1

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[list[int]]:
    return [[int(x) for x in line.split()] for line in data.split("\n\n")]


def part_1(data: list[list[int]]) -> int:
    return max(sum(x) for x in data)


def part_2(data: list[list[int]]) -> int:
    return sum(sorted((sum(x) for x in data), reverse=True)[:3])


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
