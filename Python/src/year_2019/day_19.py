# https://adventofcode.com/2019/day/19

from src.util.inputs import Inputs
from src.util.solution import Solution
from src.year_2019.intcode import IntcodeComputer


class Solution2019Day19(Solution):

    def solve(self, inputs: Inputs) -> None:
        self.result_1 = self.solve_1(inputs.input)
        self.result_2 = self.solve_2(inputs.input)

    @staticmethod
    def solve_1(program: str) -> int:
        n_affected = 0
        for x in range(50):
            for y in range(50):
                n_affected += IntcodeComputer(program).run(x, y)[0]
        return n_affected

    @staticmethod
    def solve_2(program: str) -> int:
        # Since the square's height is 100, I start by searching for the leftmost position
        # that is covered by the beam at y=100.
        x = 0
        y = 99
        for x in range(100):
            if IntcodeComputer(program).run(x, y)[0]:
                break

        # Start at the leftmost affected position in the bottom row.
        # If a hit is detected, check the space diagonally opposite of the square.
        # If that hits, then the square fits.
        # If not, go down once, then go right until the next hit is detected.
        while True:
            for x in range(x, y):
                if IntcodeComputer(program).run(x, y)[0]:
                    break
            top = y - 99
            right = x + 99
            if IntcodeComputer(program).run(right, top)[0]:
                # y - 99 because I need the top left position
                return x * 10000 + y - 99
            y += 1
