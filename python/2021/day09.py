# https://adventofcode.com/2021/day/9


from collections import namedtuple
from math import prod


SAMPLE_PATH = "../../input/2021-09-sample.txt"
INPUT_PATH = "../../input/2021-09-input.txt"
Point = namedtuple("Point", ("x", "y"))


def get_data(filename):
    with open(filename) as file:
        data = file.read().splitlines()
    heightmap = tuple(tuple(int(x) for x in list(line)) for line in data)
    low_points = get_low_points(heightmap)
    return heightmap, low_points


def get_neighbors(x, y, max_x, max_y):
    neighbors = []
    if x > 0:
        neighbors.append(Point(x - 1, y))
    if x < max_x:
        neighbors.append(Point(x + 1, y))
    if y > 0:
        neighbors.append(Point(x, y - 1))
    if y < max_y:
        neighbors.append(Point(x, y + 1))
    return neighbors


def get_low_points(heightmap):
    low_points = []
    max_x = len(heightmap[0]) - 1
    max_y = len(heightmap) - 1
    for y, row in enumerate(heightmap):
        for x, height in enumerate(row):
            neighbors = get_neighbors(x, y, max_x, max_y)
            if all(height < heightmap[n.y][n.x] for n in neighbors):
                low_points.append(Point(x, y))
    return low_points


def flood_fill(heightmap, origin, max_x, max_y):
    neighbors = [origin]
    basin_members = {origin}
    while neighbors:
        current = neighbors.pop()
        new_neighbors = get_neighbors(current.x, current.y, max_x, max_y)
        for nn in new_neighbors:
            # Assuming all basins are surrounded by nines, which is true for the sample.
            if nn not in basin_members and heightmap[nn.y][nn.x] < 9:
                neighbors.append(nn)
                basin_members.add(nn)
    return len(basin_members)


def part_1(heightmap, low_points):
    return sum(heightmap[lp.y][lp.x] + 1 for lp in low_points)


def part_2(heightmap, low_points):
    max_x = len(heightmap[0]) - 1
    max_y = len(heightmap) - 1
    basin_sizes = [flood_fill(heightmap, lp, max_x, max_y) for lp in low_points]
    basin_sizes.sort(reverse=True)
    return prod(basin_sizes[:3])


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(*sample_data) == 15
    assert part_2(*sample_data) == 1134

    challenge_data = get_data(INPUT_PATH)
    print(part_1(*challenge_data))  # 554
    print(part_2(*challenge_data))  # 1017792
