# https://adventofcode.com/2021/day/5

from collections import Counter
from itertools import chain
from re import findall
from typing import NamedTuple

from src.util.types import Data, Point2, Solution


Line = NamedTuple("Line", (("start", Point2), ("end", Point2)))


def prepare_data(data: str) -> list[Line]:
    lines = data.splitlines()
    positions = ([int(x) for x in findall(r"\d+", line)] for line in lines)
    return [Line(Point2(*position[:2]), Point2(*position[2:])) for position in positions]


def get_positions(line: Line) -> list[Point2]:
    positions = [line.start]
    slope_x = line.end.x - line.start.x
    slope_y = line.end.y - line.start.y
    dx = 0 if slope_x == 0 else slope_x // abs(slope_x)
    dy = 0 if slope_y == 0 else slope_y // abs(slope_y)
    pos = line.start
    while pos != line.end:
        pos = Point2(pos.x + dx, pos.y + dy)
        positions.append(pos)
    return positions


def count_overlaps(lines):
    positions = (get_positions(line) for line in lines)
    positions = chain.from_iterable(positions)
    counter = Counter(positions)
    return sum(count > 1 for key, count in counter.items())


def part_1(lines):
    lines = (line for line in lines if line.start.x == line.end.x or line.start.y == line.end.y)
    return count_overlaps(lines)


def part_2(lines):
    return count_overlaps(lines)


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
