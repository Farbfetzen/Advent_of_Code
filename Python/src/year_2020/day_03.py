# https://adventofcode.com/2020/day/3

from math import prod

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2020Day03(Solution):

    def solve(self, inputs: Inputs) -> None:
        map_of_trees = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(map_of_trees))

        map_of_trees = self.prepare(inputs.input)
        self.result_1 = self.solve_1(map_of_trees)
        self.result_2 = self.solve_2(map_of_trees)

    @staticmethod
    def prepare(data: str) -> list[list[bool]]:
        return [[x == "#" for x in line] for line in data.splitlines()]

    def solve_1(self, map_of_trees: list[list[bool]]) -> int:
        return self.check_slope(map_of_trees, (3, 1))

    def solve_2(self, map_of_trees: list[list[bool]]) -> int:
        slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
        n_trees = (self.check_slope(map_of_trees, slope) for slope in slopes)
        return prod(n_trees)

    @staticmethod
    def check_slope(map_of_trees: list[list[bool]], slope: tuple[int, int]) -> int:
        width = len(map_of_trees[0])
        height = len(map_of_trees)
        right, down = slope
        x = right % width
        y = down
        n_trees = 0
        while y < height:
            n_trees += map_of_trees[y][x]
            x = (x + right) % width
            y += down
        return n_trees
