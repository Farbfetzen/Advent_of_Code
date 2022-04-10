# https://adventofcode.com/2021/day/7

from math import ceil, floor
from statistics import mean, median

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[int]:
    return [int(x) for x in data.split(",")]


def part_1(positions):
    best_position = int(median(positions))
    return sum(abs(pos - best_position) for pos in positions)


def part_2(positions):
    mean_position = mean(positions)
    # Because the positions have to be ints I need to check both around the mean.
    best_positions = (floor(mean_position), ceil(mean_position))
    fuel_requirements = [0, 0]
    for i, bp in enumerate(best_positions):
        fuel = 0
        for pos in positions:
            steps = abs(pos - bp)
            fuel += steps * (steps + 1) // 2
        fuel_requirements[i] = fuel
    return int(min(fuel_requirements))


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
