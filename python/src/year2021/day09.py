# https://adventofcode.com/2021/day/9

from math import prod

from src.util.types import Data, Point2, Solution


def prepare_data(data: str) -> tuple[tuple[tuple[int, ...], ...], list[Point2]]:
    heightmap = tuple(tuple(int(x) for x in list(line)) for line in data.splitlines())
    low_points = get_low_points(heightmap)
    return heightmap, low_points


def get_neighbors(x, y, max_x, max_y):
    neighbors = []
    if x > 0:
        neighbors.append(Point2(x - 1, y))
    if x < max_x:
        neighbors.append(Point2(x + 1, y))
    if y > 0:
        neighbors.append(Point2(x, y - 1))
    if y < max_y:
        neighbors.append(Point2(x, y + 1))
    return neighbors


def get_low_points(heightmap: tuple[tuple[int, ...], ...]) -> list[Point2]:
    low_points = []
    max_x = len(heightmap[0]) - 1
    max_y = len(heightmap) - 1
    for y, row in enumerate(heightmap):
        for x, height in enumerate(row):
            neighbors = get_neighbors(x, y, max_x, max_y)
            if all(height < heightmap[n.y][n.x] for n in neighbors):
                low_points.append(Point2(x, y))
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


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(*sample_data))
    solution.samples_part_2.append(part_2(*sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(*challenge_data)
    solution.part_2 = part_2(*challenge_data)
    return solution
