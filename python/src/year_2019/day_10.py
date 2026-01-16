# https://adventofcode.com/2019/day/10

import collections
import itertools
import math

from src.util.exceptions import ResultExpectedError
from src.util.inputs import Inputs
from src.util.solution import Solution


type Position = tuple[int, int]


class Solution2019Day10(Solution):

    def solve(self, inputs: Inputs) -> None:
        visibility_map, station_position = self.create_visibility_map(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(visibility_map))
        self.sample_results_2.append(self.solve_2(visibility_map, station_position))

        visibility_map, station_position = self.create_visibility_map(inputs.input)
        self.result_1 = self.solve_1(visibility_map)
        self.result_2 = self.solve_2(visibility_map, station_position)

    def create_visibility_map(self, map_str: str) -> tuple[dict[Position, list[Position]], Position]:
        asteroid_map: list[Position] = []
        for y, line in enumerate(map_str.splitlines()):
            for x, char in enumerate(line):
                if char == "#":
                    asteroid_map.append((x, y))
        max_visible = 0
        most_unique_slopes: dict[Position, list[Position]] = {}
        best_position: Position = (0, 0)
        for a in asteroid_map:
            unique_slopes = self.get_unique_slopes(a, asteroid_map)
            visible = len(unique_slopes)
            if visible > max_visible:
                max_visible = visible
                most_unique_slopes = unique_slopes
                best_position = a
        return most_unique_slopes, best_position

    @staticmethod
    def get_unique_slopes(asteroid: Position, asteroid_map: list[Position]) -> dict:
        unique_slopes = {}
        for other in asteroid_map:
            if other == asteroid:
                continue
            slope = (other[0] - asteroid[0], other[1] - asteroid[1])
            slope_gcd = math.gcd(*slope)
            slope = (slope[0] // slope_gcd, slope[1] // slope_gcd)
            if slope in unique_slopes:
                unique_slopes[slope].append(other)
            else:
                unique_slopes[slope] = [other]
        return unique_slopes

    @staticmethod
    def solve_1(visibility_map: dict[Position, list[Position]]) -> int:
        return len(visibility_map)

    @staticmethod
    def solve_2(visibility_map: dict[Position, list[Position]], station_position: Position) -> int:
        slope_map: dict[float, list[Position]] = {}
        for slope in list(visibility_map.keys()):
            # The laser shooting starts straight up and rotates clockwise. This
            # means the angles have to be sorted accordingly.
            angle = math.atan2(-slope[1], slope[0])
            if angle > math.pi / 2:
                angle -= math.pi * 2
            angle *= -1
            slope_map[angle] = visibility_map.pop(slope)
        for v in slope_map.values():
            v.sort(
                key=(lambda x: abs(x[0] - station_position[0]) + abs(x[1] - station_position[1])),
                reverse=True,
            )
        n = 0
        slope_map = collections.OrderedDict(sorted(slope_map.items()))
        for asteroids in itertools.cycle(slope_map.values()):
            if len(asteroids) > 0:
                n += 1
                vaporized_asteroid = asteroids.pop()
                if n == 200:
                    return vaporized_asteroid[0] * 100 + vaporized_asteroid[1]
        raise ResultExpectedError
