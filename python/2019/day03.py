# https://adventofcode.com/2019/day/3


import math
import re


SAMPLE_PATH = "../../input/2019-03-sample.txt"
INPUT_PATH = "../../input/2019-03-input.txt"


def get_data(filename):
    with open(filename) as file:
        return file.read().split("\n\n")


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


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(sample_data[0]) == 159
    assert part_1(sample_data[1]) == 135
    assert part_2(sample_data[0]) == 610
    assert part_2(sample_data[1]) == 410

    challenge_data = get_data(INPUT_PATH)[0]
    print(part_1(challenge_data))  # 489
    print(part_2(challenge_data))  # 93654
