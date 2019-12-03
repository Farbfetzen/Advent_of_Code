# https://adventofcode.com/2019/day/3


import re


def construct_path(wire):
    pattern = re.compile(r"(\D+)(\d+)")
    directions = ""
    for segment in wire:
        direction, length = pattern.findall(segment)[0]
        for _ in range(int(length)):
            directions += direction
    x = 0
    y = 0
    path = [(x, y)]
    for direction in directions:
        if direction == "R":
            x += 1
        elif direction == "L":
            x -= 1
        elif direction == "U":
            y += 1
        elif direction == "D":
            y -= 1
        else:
            raise ValueError("unexpected direction")
        path.append((x, y))
    return path


def get_closest_crossing_distance(paths):
    crossings = set(paths[0]) & set(paths[1])
    crossings.remove((0, 0))
    manhattan_distances = [abs(x) + abs(y) for x, y in crossings]

    return min(manhattan_distances)


def part_1(wire_input):
    wires = [wire.split(",") for wire in wire_input.splitlines()]
    paths = [construct_path(wire) for wire in wires]
    return get_closest_crossing_distance(paths)


test1 = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83
"""
assert part_1(test1) == 159
test2 = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
"""
assert part_1(test2) == 135


with open("day_03_input.txt", "r") as file:
    wires = file.read()

print(part_1(wires))
