# https://adventofcode.com/2019/day/5

from src.util.inputs import Inputs
from src.util.solution import Solution
from src.year_2019.intcode import IntcodeComputer


class Solution2019Day05(Solution):

    def solve(self, inputs: Inputs) -> None:
        self.result_1 = self.solve_1(inputs.input)
        self.result_2 = self.solve_2(inputs.input)

    @staticmethod
    def solve_1(program: str) -> int:
        computer = IntcodeComputer(program)
        *diagnostic, result = computer.run(1)
        assert all(x == 0 for x in diagnostic)
        return result

    @staticmethod
    def solve_2(program: str) -> int:
        computer = IntcodeComputer(program)
        return computer.run(5)[0]
