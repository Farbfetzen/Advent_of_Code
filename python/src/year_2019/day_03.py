# https://adventofcode.com/2019/day/3

import math
import re

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2019Day03(Solution):

    def solve(self, inputs: Inputs) -> None:
        for sample in inputs.samples:
            wire_input = sample.splitlines()
            self.sample_results_1.append(self.solve_1(wire_input))
            self.sample_results_2.append(self.solve_2(wire_input))

        wire_input = inputs.input.splitlines()
        self.result_1 = self.solve_1(wire_input)
        self.result_2 = self.solve_2(wire_input)

    @staticmethod
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

    @staticmethod
    def get_crossings(paths: list[list[tuple[int, int]]]) -> set[tuple[int, int]]:
        crossings = set(paths[0]) & set(paths[1])
        crossings.remove((0, 0))
        return crossings

    @staticmethod
    def get_closest_crossing_distance(crossings: set[tuple[int, int]]) -> int:
        manhattan_distances = [abs(x) + abs(y) for x, y in crossings]
        return min(manhattan_distances)

    def solve_1(self, wire_input: list[str]) -> int:
        paths = self.construct_paths(wire_input)
        crossings = self.get_crossings(paths)
        return self.get_closest_crossing_distance(crossings)

    def solve_2(self, wire_input: list[str]) -> int:
        paths = self.construct_paths(wire_input)
        crossings = self.get_crossings(paths)
        smallest_distance = math.inf
        for crossing in crossings:
            distance = 0
            for path in paths:
                distance += path.index(crossing)
            if distance < smallest_distance:
                smallest_distance = distance
        return int(smallest_distance)
