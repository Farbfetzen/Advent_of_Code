# https://adventofcode.com/2021/day/22


import re


SAMPLE_PATH = "../../input/2021-22-sample.txt"
INPUT_PATH = "../../input/2021-22-input.txt"


class Cuboid:

    def __init__(self, is_on, x_min, x_max, y_min, y_max, z_min, z_max):
        self.is_on = is_on
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.z_min = z_min
        self.z_max = z_max

    def get_volume(self):
        volume = (self.x_max - self.x_min) * (self.y_max - self.y_min) * (self.z_max - self.z_min)
        return volume if self.is_on else -volume

    def get_intersection(self, other):
        """If this cuboid intersects with other cuboid, returns a new cuboid that
        matches the space covered by both. Otherwise, returns None.
        """
        if (self.x_min < other.x_max and self.x_max > other.x_min and
                self.y_min < other.y_max and self.y_max > other.y_min and
                self.z_min < other.z_max and self.z_max > other.z_min):
            return Cuboid(
                not self.is_on,
                self.x_min if other.x_min <= self.x_min < other.x_max else other.x_min,
                self.x_max if other.x_min <= self.x_max < other.x_max else other.x_max,
                self.y_min if other.y_min <= self.y_min < other.y_max else other.y_min,
                self.y_max if other.y_min <= self.y_max < other.y_max else other.y_max,
                self.z_min if other.z_min <= self.z_min < other.z_max else other.z_min,
                self.z_max if other.z_min <= self.z_max < other.z_max else other.z_max
            )


def get_data(filename):
    with open(filename) as file:
        inputs = file.read().split("\n\n")
    data = []
    for chunk in inputs:
        cuboids = []
        for line in chunk.splitlines():
            is_on = line.startswith("on")
            x_min, x_max, y_min, y_max, z_min, z_max = (int(n) for n in re.findall(r"-?\d+", line))
            # The input specifies coordinates as the left edges of the cube cells.
            # Therefore, I need to add one to the maximum coordinates to get the correct borders.
            cuboids.append(Cuboid(is_on, x_min, x_max + 1, y_min, y_max + 1, z_min, z_max + 1))
        data.append(cuboids)
    return data


def reboot_reactor(cuboids):
    all_cuboids = []
    for cuboid in cuboids:
        intersections = check_intersections(cuboid, all_cuboids)
        all_cuboids.extend(intersections)
        if cuboid.is_on:
            all_cuboids.append(cuboid)
    return sum(cuboid.get_volume() for cuboid in all_cuboids)


def check_intersections(cuboid, candidates):
    new_cuboids = []
    for candidate in candidates:
        intersection = candidate.get_intersection(cuboid)
        if intersection is not None:
            new_cuboids.append(intersection)
    return new_cuboids


def part_1(cuboids):
    initialization_cuboids = [
        cuboid for cuboid in cuboids
        if cuboid.x_min >= -50 and cuboid.x_max <= 51
        and cuboid.y_min >= -50 and cuboid.y_max <= 51
        and cuboid.z_min >= -50 and cuboid.z_max <= 51
    ]
    return reboot_reactor(initialization_cuboids)


def part_2(cuboids):
    return reboot_reactor(cuboids)


if __name__ == "__main__":
    # Instead of cutting the cuboids into smaller pieces I just add negative
    # volumes for some intersections. I saw this brilliant idea on Reddit and
    # had to implement it.

    sample_data = get_data(SAMPLE_PATH)
    assert part_1(sample_data[0]) == 39
    assert part_1(sample_data[1]) == 590784
    assert part_1(sample_data[2]) == 474140
    assert part_2(sample_data[2]) == 2758514936282235

    challenge_data = get_data(INPUT_PATH)[0]
    print(part_1(challenge_data))  # 620241
    print(part_2(challenge_data))  # 1284561759639324
