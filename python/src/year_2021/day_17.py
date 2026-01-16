# https://adventofcode.com/2021/day/17

import itertools
import re

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2021Day17(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(prepared_input[2]))
        self.sample_results_2.append(self.solve_2(*prepared_input))

        prepared_input = self.prepare(inputs.input)
        self.result_1 = self.solve_1(prepared_input[2])
        self.result_2 = self.solve_2(*prepared_input)

    @staticmethod
    def prepare(data: str) -> list[int]:
        return [int(x) for x in re.findall(r"-?\d+", data)]

    @staticmethod
    def solve_1(y_min: int) -> int:
        """The probe must return to the starting position with the starting y-velocity negated.
        In the next step it must not go further than the lowest allowed target coordinate.
        Therefore, it should be launched upwards at a speed of min_y - 1.
        So all I have to do is sum the values from 1 to min_y - 1.
        """
        return y_min * (y_min + 1) // 2

    @staticmethod
    def solve_2(x_min: int, x_max: int, y_min: int, y_max: int) -> int:
        """Simple brute force."""
        valid_velocities_count = 0
        for x_velocity_initial, y_velocity_initial in itertools.product(range(x_max + 1), range(y_min, -y_min)):
            x = 0
            y = 0
            x_velocity = x_velocity_initial
            y_velocity = y_velocity_initial
            while x <= x_max and y >= y_min:
                if x_min <= x and y <= y_max:
                    valid_velocities_count += 1
                    break
                x += x_velocity
                y += y_velocity
                if x_velocity > 0:
                    x_velocity -= 1
                elif x_velocity < 0:
                    x_velocity += 1
                y_velocity -= 1
        return valid_velocities_count
