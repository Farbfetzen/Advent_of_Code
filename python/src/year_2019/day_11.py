# https://adventofcode.com/2019/day/11

import collections
from collections.abc import KeysView

from src.util.inputs import Inputs
from src.util.solution import Solution
from src.util.vector import Vector2
from src.year_2019.intcode import IntcodeComputer


type Panels = dict[Vector2, int]


class Solution2019Day11(Solution):

    def solve(self, inputs: Inputs) -> None:
        self.result_1 = self.solve_1(inputs.input)
        self.result_2 = self.solve_2(inputs.input)

    def solve_1(self, program: str) -> int:
        return len(self.paint(IntcodeComputer(program), 0))

    def solve_2(self, program: str) -> str:
        panels = self.paint(IntcodeComputer(program), 1)
        min_x, max_x, min_y, max_y = self.get_min_max(panels.keys())
        width = max_x - min_x + 1
        height = max_y - min_y + 1
        min_position = Vector2(min_x, min_y)
        registration = [[" "] * width for _ in range(height)]
        for position, color in panels.items():
            if color == 1:
                position -= min_position
                registration[position.y][position.x] = "█"
        return "\n".join("".join(line) for line in registration)

    @staticmethod
    def paint(robot: IntcodeComputer, starting_color: int) -> Panels:
        position = Vector2(0, 0)
        direction = Vector2(0, -1)
        panels: Panels = collections.defaultdict(int, {position: starting_color})
        while not robot.halted:
            new_color, turn = robot.run(panels[position])
            panels[position] = new_color
            direction = direction.turn_left() if turn == 0 else direction.turn_right()
            position += direction
        return panels

    @staticmethod
    def get_min_max(coordinates: KeysView[Vector2]) -> tuple[int, int, int, int]:
        """Return the extreme coordinates of the painted panels."""
        iterator = iter(coordinates)
        first = next(iterator)
        min_x = max_x = first.x
        min_y = max_y = first.y
        for position in iterator:
            if position.x < min_x:
                min_x = position.x
            elif position.x > max_x:
                max_x = position.x
            if position.y < min_y:
                min_y = position.y
            elif position.y > max_y:
                max_y = position.y
        return min_x, max_x, min_y, max_y
