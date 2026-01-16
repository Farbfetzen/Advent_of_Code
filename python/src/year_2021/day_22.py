# https://adventofcode.com/2021/day/22
import re
from typing import Self

from src.util.inputs import Inputs
from src.util.solution import Solution


class Cuboid:

    def __init__(self, is_on: bool, x_min: int, x_max: int, y_min: int, y_max: int, z_min: int, z_max: int):
        self.is_on = is_on
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.z_min = z_min
        self.z_max = z_max

    def get_volume(self) -> int:
        volume = (self.x_max - self.x_min) * (self.y_max - self.y_min) * (self.z_max - self.z_min)
        return volume if self.is_on else -volume

    def get_intersection(self, other: Self) -> Self | None:
        """If this cuboid intersects with other cuboid, returns a new cuboid that
        matches the space covered by both. Otherwise, returns None.
        """
        if (
            self.x_min < other.x_max
            and self.x_max > other.x_min
            and self.y_min < other.y_max
            and self.y_max > other.y_min
            and self.z_min < other.z_max
            and self.z_max > other.z_min
        ):
            return Cuboid(
                not self.is_on,
                self.x_min if other.x_min <= self.x_min < other.x_max else other.x_min,
                self.x_max if other.x_min <= self.x_max < other.x_max else other.x_max,
                self.y_min if other.y_min <= self.y_min < other.y_max else other.y_min,
                self.y_max if other.y_min <= self.y_max < other.y_max else other.y_max,
                self.z_min if other.z_min <= self.z_min < other.z_max else other.z_min,
                self.z_max if other.z_min <= self.z_max < other.z_max else other.z_max,
            )
        return None


class Solution2021Day22(Solution):

    def solve(self, inputs: Inputs) -> None:
        # Instead of cutting the cuboids into smaller pieces I just add negative
        # volumes for some intersections. I saw this brilliant idea on Reddit and
        # had to implement it.
        for i, sample in enumerate(inputs.samples):
            prepared_input = self.prepare(sample)
            self.sample_results_1.append(self.solve_1(prepared_input))
            if i == 2:
                self.sample_results_2.append(self.solve_2(prepared_input))

        prepared_input = self.prepare(inputs.input)
        self.result_1 = self.solve_1(prepared_input)
        self.result_2 = self.solve_2(prepared_input)

    @staticmethod
    def prepare(data: str) -> list[Cuboid]:
        cuboids = []
        for line in data.splitlines():
            is_on = line.startswith("on")
            x_min, x_max, y_min, y_max, z_min, z_max = (int(n) for n in re.findall(r"-?\d+", line))
            # The input specifies coordinates as the left edges of the cube cells.
            # Therefore, I need to add one to the maximum coordinates to get the correct borders.
            cuboids.append(Cuboid(is_on, x_min, x_max + 1, y_min, y_max + 1, z_min, z_max + 1))
        return cuboids

    def solve_1(self, cuboids: list[Cuboid]) -> int:
        initialization_cuboids = [
            cuboid
            for cuboid in cuboids
            if cuboid.x_min >= -50
            and cuboid.x_max <= 51
            and cuboid.y_min >= -50
            and cuboid.y_max <= 51
            and cuboid.z_min >= -50
            and cuboid.z_max <= 51
        ]
        return self.reboot_reactor(initialization_cuboids)

    def solve_2(self, cuboids: list[Cuboid]) -> int:
        return self.reboot_reactor(cuboids)

    def reboot_reactor(self, cuboids: list[Cuboid]):
        all_cuboids = []
        for cuboid in cuboids:
            intersections = self.check_intersections(cuboid, all_cuboids)
            all_cuboids.extend(intersections)
            if cuboid.is_on:
                all_cuboids.append(cuboid)
        return sum(cuboid.get_volume() for cuboid in all_cuboids)

    @staticmethod
    def check_intersections(cuboid: Cuboid, candidates: list[Cuboid]) -> list[Cuboid]:
        new_cuboids = []
        for candidate in candidates:
            intersection = candidate.get_intersection(cuboid)
            if intersection is not None:
                new_cuboids.append(intersection)
        return new_cuboids
