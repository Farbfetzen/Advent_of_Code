# https://adventofcode.com/2021/day/25

from src.util.inputs import Inputs
from src.util.solution import Solution
from src.util.util import Point2


class Solution2021Day25(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(*prepared_input))

        prepared_input = self.prepare(inputs.input)
        self.result_1 = self.solve_1(*prepared_input)
        self.result_2 = "No part 2 on day 25. Merry Christmas!"

    @staticmethod
    def prepare(data: str) -> tuple[set[Point2], set[Point2], int, int]:
        data_list = data.splitlines()
        cucumbers_right = set()
        cucumbers_down = set()
        for y, row in enumerate(data_list):
            for x, char in enumerate(row):
                if char == ">":
                    cucumbers_right.add(Point2(x, y))
                elif char == "v":
                    cucumbers_down.add(Point2(x, y))
        width = len(data_list[0])
        height = len(data_list)
        return cucumbers_right, cucumbers_down, width, height

    @staticmethod
    def solve_1(cucumbers_right: set[Point2], cucumbers_down: set[Point2], width: int, height: int) -> int:
        steps = 0
        while True:
            steps += 1
            move_right = []
            for x, y in cucumbers_right:
                new_position = Point2((x + 1) % width, y)
                if new_position not in cucumbers_right and new_position not in cucumbers_down:
                    move_right.append((Point2(x, y), new_position))
            for position, new_position in move_right:
                cucumbers_right.remove(position)
                cucumbers_right.add(new_position)
            move_down = []
            for x, y in cucumbers_down:
                new_position = Point2(x, (y + 1) % height)
                if new_position not in cucumbers_down and new_position not in cucumbers_right:
                    move_down.append(((x, y), new_position))
            for position, new_position in move_down:
                cucumbers_down.remove(position)
                cucumbers_down.add(new_position)
            if not move_right and not move_down:
                return steps
