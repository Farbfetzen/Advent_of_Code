# https://adventofcode.com/2021/day/19

import itertools
from collections.abc import Iterator
from typing import Self

from src.util.inputs import Inputs
from src.util.solution import Solution


class IntVector3:

    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def rotate_around_x(self) -> None:
        self.x, self.y, self.z = self.x, -self.z, self.y

    def rotate_around_y(self) -> None:
        self.x, self.y, self.z = self.z, self.y, -self.x

    def rotate_around_z(self) -> None:
        self.x, self.y, self.z = self.y, -self.x, self.z

    def translate(self, translation_vector) -> None:
        self.x += translation_vector.x
        self.y += translation_vector.y
        self.z += translation_vector.z

    def distance_to(self, other: Self) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other: Self) -> Self:
        return IntVector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Self) -> Self:
        return IntVector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z


class Scanner:

    def __init__(self, beacon_positions: list[IntVector3]) -> None:
        self.beacon_positions = beacon_positions
        self.distances = {a.distance_to(b) for a, b in itertools.combinations(self.beacon_positions, 2)}
        self.position = None

    def generate_all_rotations(self) -> Iterator[None]:
        # (original orientation,
        # x, x, x, xy,
        # x, x, x, xy,
        # x, x, x, xy,
        # x, x, x, xyz,
        # x, x, x, xzz,
        # x, x, x)
        yield  # original orientation
        for i in range(1, 24):
            for position in self.beacon_positions:
                position.rotate_around_x()
            if i == 4 or i == 8 or i == 12:
                for position in self.beacon_positions:
                    position.rotate_around_y()
            elif i == 16:
                for position in self.beacon_positions:
                    position.rotate_around_y()
                    position.rotate_around_z()
            elif i == 20:
                for position in self.beacon_positions:
                    position.rotate_around_z()
                    position.rotate_around_z()
            yield


class Solution2021Day19(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(prepared_input))
        self.sample_results_2.append(self.solve_2(prepared_input))

        prepared_input = self.prepare(inputs.input)
        self.result_1 = self.solve_1(prepared_input)
        self.result_2 = self.solve_2(prepared_input)

    @staticmethod
    def prepare(data: str) -> list[Scanner]:
        scanners = []
        for scanner_report in data.split("\n\n"):
            positions = []
            for line in scanner_report.splitlines()[1:]:
                positions.append(IntVector3(*(int(n) for n in line.split(","))))
            scanners.append(Scanner(positions))
        return scanners

    def solve_1(self, scanners: list[Scanner]) -> int:
        self.align_scanners(scanners)
        unique_beacons = set()
        for scanner in scanners:
            for beacon in scanner.beacon_positions:
                unique_beacons.add(str(beacon))
        return len(unique_beacons)

    @staticmethod
    def solve_2(scanners: list[Scanner]) -> int:
        max_distance = 0
        for a, b in itertools.combinations(scanners, 2):
            max_distance = max(a.position.distance_to(b.position), max_distance)
        return max_distance

    # noinspection PyUnboundLocalVariable
    def align_scanners(self, scanners: list[Scanner]) -> None:
        scanner_0 = scanners[0]
        scanner_0.position = IntVector3(0, 0, 0)
        fixed_scanners = [scanner_0]
        scanners_todo = scanners[1:]
        while scanners_todo:
            for current_scanner, fixed_scanner in itertools.product(scanners_todo, fixed_scanners):
                # 12 Points have 12 * 11 / 2 = 66 pairwise distances
                # If the points are the same then the distances between them should be the same.
                if len(current_scanner.distances.intersection(fixed_scanner.distances)) < 66:
                    continue
                translation_vector = self.find_alignment(current_scanner, fixed_scanner)
                if translation_vector is not None:
                    break
            scanners_todo.remove(current_scanner)
            fixed_scanners.append(current_scanner)
            # translation_vector is the position of current_scanner relative to scanner 0.
            current_scanner.position = translation_vector
            for position in current_scanner.beacon_positions:
                position.translate(translation_vector)

    @staticmethod
    def find_alignment(current_scanner: Scanner, fixed_scanner: Scanner) -> IntVector3 | None:
        for _ in current_scanner.generate_all_rotations():
            # Skip the first 11 beacons because only one matching anchor position is necessary.
            beacons = itertools.product(fixed_scanner.beacon_positions[11:], current_scanner.beacon_positions)
            for fixed_beacon, variable_beacon in beacons:
                translation_vector = fixed_beacon - variable_beacon
                n_matching = 0
                for i, pos in enumerate(current_scanner.beacon_positions):
                    b_shifted = pos + translation_vector
                    if b_shifted in fixed_scanner.beacon_positions:
                        n_matching += 1
                    if n_matching == 12:
                        return translation_vector
                    if len(current_scanner.beacon_positions) - i < 12 - n_matching:
                        # Not enough beacons left to get to 12.
                        break
