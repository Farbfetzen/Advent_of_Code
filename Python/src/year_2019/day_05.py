# https://adventofcode.com/2019/day/5

from src.util.inputs import Inputs
from src.util.solution import Solution
from src.year_2019.intcode import IntcodeComputer


class Solution2019Day05(Solution):

    def solve(self, inputs: Inputs) -> None:
        program = [int(i) for i in inputs.input.split(",")]
        self.result_1 = self.solve_1(program)
        self.result_2 = self.solve_2(program)

    @staticmethod
    def solve_1(program: list[int]) -> int:
        computer = IntcodeComputer(program, [1])
        computer.run()
        *diagnostic, result = computer.output
        assert all(x == 0 for x in diagnostic)
        return result

    @staticmethod
    def solve_2(program: list[int]) -> int:
        computer = IntcodeComputer(program, [5])
        computer.run()
        return computer.output[0]
