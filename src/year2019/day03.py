# https://adventofcode.com/2019/day/3

import math
import re

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[str]:
    return data.splitlines()


def construct_paths(wire_input: list[str]) -> list[list[tuple[int, int]]]:
    wires = [wire.split(",") for wire in wire_input]
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


def get_crossings(paths: list[list[tuple[int, int]]]) -> set[tuple[int, int]]:
    crossings = set(paths[0]) & set(paths[1])
    crossings.remove((0, 0))
    return crossings


def get_closest_crossing_distance(crossings: set[tuple[int, int]]) -> int:
    manhattan_distances = [abs(x) + abs(y) for x, y in crossings]
    return min(manhattan_distances)


def part_1(wire_input: list[str]) -> int:
    paths = construct_paths(wire_input)
    crossings = get_crossings(paths)
    return get_closest_crossing_distance(crossings)


def part_2(wire_input: list[str]) -> int:
    paths = construct_paths(wire_input)
    crossings = get_crossings(paths)
    smallest_distance = math.inf
    for crossing in crossings:
        distance = 0
        for path in paths:
            distance += path.index(crossing)
        if distance < smallest_distance:
            smallest_distance = distance
    return int(smallest_distance)


def solve(data: Data) -> Solution:
    solution = Solution()
    for sample in data.samples:
        sample_data = prepare_data(sample)
        solution.samples_part_1.append(part_1(sample_data))
        solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
