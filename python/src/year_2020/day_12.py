# https://adventofcode.com/2020/day/12

import os


os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame

from src.util.inputs import Inputs
from src.util.solution import Solution
from typing import Literal


class Solution2020Day12(Solution):

    def solve(self, inputs: Inputs) -> None:
        instructions = inputs.samples[0].splitlines()
        self.sample_results_1.append(self.navigate(instructions, 1))
        self.sample_results_2.append(self.navigate(instructions, 2))

        instructions = inputs.input.splitlines()
        self.result_1 = self.navigate(instructions, 1)
        self.result_2 = self.navigate(instructions, 2)

    @staticmethod
    def navigate(instructions: list[str], part: Literal[1, 2] = 1) -> int:
        position = pygame.Vector2(0, 0)
        # "direction_or_waypoint" is either the ship direction in part 1
        # or the waypoint position relative to the ship in part 2.
        direction_or_waypoint = pygame.Vector2(1, 0) if part == 1 else pygame.Vector2(10, -1)
        # IMPORTANT: This uses coordinates where y increases downwards,
        # which also inverts the rotations!
        cardinal_directions = {
            "N": pygame.Vector2(0, -1),
            "S": pygame.Vector2(0, 1),
            "W": pygame.Vector2(-1, 0),
            "E": pygame.Vector2(1, 0),
        }
        for instruction in instructions:
            action = instruction[0]
            value = int(instruction[1:])
            if action in cardinal_directions:
                if part == 1:
                    position += cardinal_directions[action] * value
                else:
                    direction_or_waypoint += cardinal_directions[action] * value
            elif action == "L":
                direction_or_waypoint.rotate_ip(-value)
            elif action == "R":
                direction_or_waypoint.rotate_ip(value)
            elif action == "F":
                position += direction_or_waypoint * value
        return int(abs(position.x) + abs(position.y))
