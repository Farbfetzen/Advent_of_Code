# https://adventofcode.com/2019/day/9

from src.util.inputs import Inputs
from src.util.solution import Solution
from src.year_2019.intcode import IntcodeComputer


class Solution2019Day09(Solution):

    def solve(self, inputs: Inputs) -> None:
        self.sample_results_other["copy program"] = self.test_computer(inputs.samples[0])
        self.sample_results_1.append(self.test_computer(inputs.samples[1])[0])
        self.sample_results_1.append(self.test_computer(inputs.samples[2])[0])

        self.result_1 = self.solve_1(inputs.input)
        self.result_2 = self.solve_2(inputs.input)

    @staticmethod
    def test_computer(program: str) -> list[int]:
        return IntcodeComputer(program).run()

    @staticmethod
    def solve_1(program: str) -> int:
        return IntcodeComputer(program).run(1)[0]

    @staticmethod
    def solve_2(program: str) -> int:
        return IntcodeComputer(program).run(2)[0]
