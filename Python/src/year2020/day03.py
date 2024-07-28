# https://adventofcode.com/2020/day/3

from math import prod

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[list[bool]]:
    return [[x == "#" for x in line] for line in data.splitlines()]


def check_slope(data, slope):
    width = len(data[0])
    height = len(data)
    right, down = slope
    x = right % width
    y = down
    n_trees = 0
    while y < height:
        n_trees += data[y][x]
        x = (x + right) % width
        y += down
    return n_trees


def part_1(map_of_trees):
    return check_slope(map_of_trees, (3, 1))


def part_2(map_of_trees):
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    n_trees = (check_slope(map_of_trees, slope) for slope in slopes)
    return prod(n_trees)


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.input)
    solution.samples_part_1.append(part_1(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
