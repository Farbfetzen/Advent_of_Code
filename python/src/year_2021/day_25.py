# https://adventofcode.com/2021/day/25

from src.util.inputs import Inputs
from src.util.solution import Solution


type CucumberMap = list[list[str]]


class Solution2021Day25(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(prepared_input))

        prepared_input = self.prepare(inputs.input)
        self.result_1 = self.solve_1(prepared_input)
        self.result_2 = "No part 2 on day 25. Merry Christmas!"

    @staticmethod
    def prepare(data: str) -> CucumberMap:
        return [list(line) for line in data.splitlines()]

    def solve_1(self, cucumber_map: CucumberMap) -> int:
        width = len(cucumber_map[0])
        height = len(cucumber_map)
        steps = 0
        moved = True
        while moved:
            steps += 1
            new_map = [row.copy() for row in cucumber_map]
            moved = self.move_right(cucumber_map, new_map, width)
            cucumber_map = [row.copy() for row in new_map]
            moved = self.move_down(cucumber_map, new_map, height, moved)
            cucumber_map = new_map
        return steps

    @staticmethod
    def move_right(cucumber_map: CucumberMap, new_map: CucumberMap, width: int) -> bool:
        moved = False
        for y, row in enumerate(cucumber_map):
            for x, cucumber in enumerate(row):
                if cucumber == ">":
                    right_x = (x + 1) % width
                    if cucumber_map[y][right_x] == ".":
                        new_map[y][right_x] = ">"
                        new_map[y][x] = "."
                        moved = True
        return moved

    @staticmethod
    def move_down(cucumber_map: CucumberMap, new_map: CucumberMap, height: int, moved: bool) -> bool:
        for y, row in enumerate(cucumber_map):
            for x, cucumber in enumerate(row):
                if cucumber == "v":
                    below_y = (y + 1) % height
                    if cucumber_map[below_y][x] == ".":
                        new_map[below_y][x] = "v"
                        new_map[y][x] = "."
                        moved = True
        return moved
