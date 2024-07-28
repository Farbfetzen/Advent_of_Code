# https://adventofcode.com/2021/day/19

from itertools import combinations, product

from src.util.types import Data, Solution


class IntVector3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def rotate_around_x(self):
        self.x, self.y, self.z = self.x, -self.z, self.y

    def rotate_around_y(self):
        self.x, self.y, self.z = self.z, self.y, -self.x

    def rotate_around_z(self):
        self.x, self.y, self.z = self.y, -self.x, self.z

    def translate(self, translation_vector):
        self.x += translation_vector.x
        self.y += translation_vector.y
        self.z += translation_vector.z

    def distance_to(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return IntVector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return IntVector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z


class Scanner:

    def __init__(self, beacon_positions):
        self.beacon_positions = beacon_positions
        self.distances = {a.distance_to(b) for a, b in combinations(self.beacon_positions, 2)}
        self.position = None

    def generate_all_rotations(self):
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


def prepare_data(data: str) -> list[Scanner]:
    scanners = []
    for scanner_report in data.split("\n\n"):
        positions = []
        for line in scanner_report.splitlines()[1:]:
            positions.append(IntVector3(*(int(n) for n in line.split(","))))
        scanners.append(Scanner(positions))
    return scanners


# noinspection PyUnboundLocalVariable
def align_scanners(scanners):
    scanner_0 = scanners[0]
    scanner_0.position = IntVector3(0, 0, 0)
    fixed_scanners = [scanner_0]
    scanners_todo = scanners[1:]
    while scanners_todo:
        for current_scanner, fixed_scanner in product(scanners_todo, fixed_scanners):
            # 12 Points have 12 * 11 / 2 = 66 pairwise distances
            # If the points are the same then the distances between them should be the same.
            if len(current_scanner.distances.intersection(fixed_scanner.distances)) < 66:
                continue
            translation_vector = find_alignment(current_scanner, fixed_scanner)
            if translation_vector is not None:
                break
        scanners_todo.remove(current_scanner)
        fixed_scanners.append(current_scanner)
        # translation_vector is the position of current_scanner relative to scanner 0.
        current_scanner.position = translation_vector
        for position in current_scanner.beacon_positions:
            position.translate(translation_vector)


def find_alignment(current_scanner, fixed_scanner):
    for _ in current_scanner.generate_all_rotations():
        # Skip the first 11 beacons because only one matching anchor position is necessary.
        for fixed_beacon, variable_beacon in product(
                fixed_scanner.beacon_positions[11:], current_scanner.beacon_positions):
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


def part_1(scanners):
    align_scanners(scanners)
    unique_beacons = set()
    for scanner in scanners:
        for beacon in scanner.beacon_positions:
            unique_beacons.add(str(beacon))
    return len(unique_beacons)


def part_2(scanners):
    max_distance = 0
    for a, b in combinations(scanners, 2):
        max_distance = max(a.position.distance_to(b.position), max_distance)
    return max_distance


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
