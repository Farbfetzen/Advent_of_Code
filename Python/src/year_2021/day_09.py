# https://adventofcode.com/2021/day/9

from math import prod

from src.util.inputs import Inputs
from src.util.solution import Solution
from src.util.util import Point2


class Solution2021Day09(Solution):

    def solve(self, inputs: Inputs) -> None:
        heightmap, low_points = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(heightmap, low_points))
        self.sample_results_2.append(self.solve_2(heightmap, low_points))

        heightmap, low_points = self.prepare(inputs.input)
        self.result_1 = self.solve_1(heightmap, low_points)
        self.result_2 = self.solve_2(heightmap, low_points)

    def prepare(self, data: str) -> tuple[tuple[tuple[int, ...], ...], list[Point2]]:
        heightmap = tuple(tuple(int(x) for x in line) for line in data.splitlines())
        low_points = self.get_low_points(heightmap)
        return heightmap, low_points

    @staticmethod
    def get_neighbors(x, y, max_x, max_y) -> list[Point2]:
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

    def get_low_points(self, heightmap: tuple[tuple[int, ...], ...]) -> list[Point2]:
        low_points = []
        max_x = len(heightmap[0]) - 1
        max_y = len(heightmap) - 1
        for y, row in enumerate(heightmap):
            for x, height in enumerate(row):
                neighbors = self.get_neighbors(x, y, max_x, max_y)
                if all(height < heightmap[n.y][n.x] for n in neighbors):
                    low_points.append(Point2(x, y))
        return low_points

    def flood_fill(self, heightmap, origin, max_x, max_y) -> int:
        neighbors = [origin]
        basin_members = {origin}
        while neighbors:
            current = neighbors.pop()
            new_neighbors = self.get_neighbors(current.x, current.y, max_x, max_y)
            for nn in new_neighbors:
                # Assuming all basins are surrounded by nines, which is true for the sample.
                if nn not in basin_members and heightmap[nn.y][nn.x] < 9:
                    neighbors.append(nn)
                    basin_members.add(nn)
        return len(basin_members)

    @staticmethod
    def solve_1(heightmap, low_points) -> int:
        return sum(heightmap[lp.y][lp.x] + 1 for lp in low_points)

    def solve_2(self, heightmap, low_points) -> int:
        max_x = len(heightmap[0]) - 1
        max_y = len(heightmap) - 1
        basin_sizes = [self.flood_fill(heightmap, lp, max_x, max_y) for lp in low_points]
        basin_sizes.sort(reverse=True)
        return prod(basin_sizes[:3])
