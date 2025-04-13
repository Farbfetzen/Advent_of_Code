# https://adventofcode.com/2019/day/13

import itertools

from src.util.inputs import Inputs
from src.util.solution import Solution
from src.year_2019.intcode import IntcodeComputer


type GameGrid = dict[tuple[int, int], int]


class Solution2019Day13(Solution):

    def solve(self, inputs: Inputs) -> None:
        arcade, n_blocks, paddle_x, ball_x = self.build_game_grid(inputs.input)
        self.result_1 = n_blocks
        self.result_2 = self.solve_2(arcade, paddle_x, ball_x)

    @staticmethod
    def build_game_grid(program: str) -> tuple[IntcodeComputer, int, int, int]:
        arcade = IntcodeComputer(program)
        arcade.memory[0] = 2
        paddle_x = -1
        ball_x = -1
        n_blocks = 0
        for x, y, tile_id in itertools.batched(arcade.run(), 3):
            if tile_id == 2:
                n_blocks += 1
            elif tile_id == 3:
                paddle_x = x
            elif tile_id == 4:
                ball_x = x
        assert paddle_x >= 0 and ball_x >= 0
        return arcade, n_blocks, paddle_x, ball_x

    @staticmethod
    def solve_2(arcade: IntcodeComputer, paddle_x: int, ball_x: int) -> int:
        score = 0
        while not arcade.halted:
            if ball_x < paddle_x:
                joystick_tilt = -1
            elif ball_x > paddle_x:
                joystick_tilt = 1
            else:
                joystick_tilt = 0
            # Each time arcade.run() is called it returns the new state of the complete game_grid.
            for x, y, value in itertools.batched(arcade.run(joystick_tilt), 3):
                if x == -1 and y == 0:
                    score = value
                elif value == 3:
                    paddle_x = x
                elif value == 4:
                    ball_x = x
        return score
