# https://adventofcode.com/2021/day/5


import collections
import itertools
import re


Point = collections.namedtuple("Point", ("x", "y"))
Line = collections.namedtuple("Line", ("start", "end"))


def get_data(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    positions = ([int(x) for x in re.findall(r"\d+", line)] for line in lines)
    return [Line(Point(*position[:2]), Point(*position[2:])) for position in positions]


def get_positions(line):
    positions = [line.start]
    slope_x = line.end.x - line.start.x
    slope_y = line.end.y - line.start.y
    dx = 0 if slope_x == 0 else slope_x // abs(slope_x)
    dy = 0 if slope_y == 0 else slope_y // abs(slope_y)
    pos = line.start
    while pos != line.end:
        pos = Point(pos.x + dx, pos.y + dy)
        positions.append(pos)
    return positions


def count_overlaps(lines):
    positions = (get_positions(line) for line in lines)
    positions = itertools.chain.from_iterable(positions)
    counter = collections.Counter(positions)
    return sum(count > 1 for key, count in counter.items())


def part_1(lines):
    lines = (line for line in lines if line.start.x == line.end.x or line.start.y == line.end.y)
    return count_overlaps(lines)


def part_2(lines):
    return count_overlaps(lines)


sample_data = get_data("../../input/2021-05-sample.txt")
challenge_data = get_data("../../input/2021-05-input.txt")

if __name__ == "__main__":
    assert part_1(sample_data) == 5
    assert part_2(sample_data) == 12

    print(part_1(challenge_data))  # 6267
    print(part_2(challenge_data))  # 20196
