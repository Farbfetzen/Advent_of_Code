# https://adventofcode.com/2019/day/15

from src.util.inputs import Inputs
from src.util.solution import Solution
from src.util.vector import Vector2
from src.year_2019.intcode import IntcodeComputer


class Solution2019Day15(Solution):

    def __init__(self) -> None:
        super().__init__()
        self.origin = Vector2(0, 0)
        self.locations = {self.origin}
        self.oxygen_system_position = Vector2(0, 0)
        # For calculating the new positions: north, east, south, west.
        self.dx_dy = (Vector2(0, -1), Vector2(1, 0), Vector2(0, 1), Vector2(-1, 0))

    def solve(self, inputs: Inputs) -> None:
        self.explore(inputs.input)
        self.flood_fill()

    def explore(self, program: str) -> None:
        """The strategy for exploring the map is to hug the left wall.
        This finds all paths as long as there are no loops.
        The map has been fully explored as soon as the droid returns to the origin.
        """
        droid = IntcodeComputer(program)
        position = self.origin
        # Directions ordered clockwise: north (1), east (4), south (2), west (3).
        directions = [1, 4, 2, 3]
        direction_index = 0
        while True:
            status = droid.run(directions[direction_index])[0]
            if status == 0:
                # hit wall, turn right
                direction_index += 1
            else:
                # calculate new position and turn left
                position += self.dx_dy[direction_index]
                direction_index -= 1
                if position == self.origin:
                    break
                self.locations.add(position)
                if status == 2:
                    self.oxygen_system_position = position
            direction_index %= 4

    def flood_fill(self) -> None:
        """Run a flood fill starting from the oxygen system."""
        frontier = {self.oxygen_system_position}
        self.locations -= frontier
        steps = 0
        while self.locations:
            steps += 1
            neighbors = {position + d for position in frontier for d in self.dx_dy}
            frontier = neighbors - frontier & self.locations
            self.locations -= frontier
            if not self.result_1 and self.origin in frontier:
                self.result_1 = steps
            if steps > 400:
                raise RuntimeError("too many steps!")
        self.result_2 = steps
