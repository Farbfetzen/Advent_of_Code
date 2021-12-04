# https://adventofcode.com/2019/day/3


import re
import math


def construct_paths(wire_input):
    wires = [wire.split(",") for wire in wire_input.splitlines()]
    paths = []
    pattern = re.compile(r"(\D+)(\d+)")
    for wire in wires:
        directions = ""
        for segment in wire:
            direction, length = pattern.findall(segment)[0]
            for _ in range(int(length)):
                directions += direction
        x = 0
        y = 0
        path = [(x, y)]
        dx = {"R": 1, "L": -1, "U": 0, "D": 0}
        dy = {"R": 0, "L": 0, "U": 1, "D": -1}
        for direction in directions:
            assert direction in "RLUD"
            x += dx[direction]
            y += dy[direction]
            path.append((x, y))
        paths.append(path)
    return paths


def get_crossings(paths):
    crossings = set(paths[0]) & set(paths[1])
    crossings.remove((0, 0))
    return crossings


def get_closest_crossing_distance(crossings):
    manhattan_distances = [abs(x) + abs(y) for x, y in crossings]
    return min(manhattan_distances)


def part_1(wire_input):
    paths = construct_paths(wire_input)
    crossings = get_crossings(paths)
    return get_closest_crossing_distance(crossings)


def part_2(wire_input):
    paths = construct_paths(wire_input)
    crossings = get_crossings(paths)
    smallest_distance = math.inf
    for crossing in crossings:
        distance = 0
        for path in paths:
            distance += path.index(crossing)
        if distance < smallest_distance:
            smallest_distance = distance
    return smallest_distance


test1 = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83
"""
assert part_1(test1) == 159
assert part_2(test1) == 610
test2 = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
"""
assert part_1(test2) == 135
assert part_2(test2) == 410


with open("../../input/2019-03-input.txt") as file:
    day_03_input = file.read()

print(part_1(day_03_input))  # 489
print(part_2(day_03_input))  # 93654
