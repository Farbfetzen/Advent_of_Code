# https://adventofcode.com/2019/day/2

from src.util.exceptions import ResultExpectedError
from src.util.inputs import Inputs
from src.util.solution import Solution
from src.year_2019.intcode import IntcodeComputer


class Solution2019Day02(Solution):

    def solve(self, inputs: Inputs) -> None:
        for i, sample in enumerate(inputs.samples):
            program = self.prepare(sample)
            computer = IntcodeComputer(program)
            computer.run()
            self.sample_results_other[f"sample {i}"] = tuple(computer.memory.values())

        program = self.prepare(inputs.input)
        self.result_1 = self.solve_1(program)
        self.result_2 = self.solve_2(program)

    @staticmethod
    def prepare(data: str) -> list[int]:
        return [int(i) for i in data.split(",")]

    @staticmethod
    def fix_program(program: list[int], noun: int, verb: int) -> None:
        program[1] = noun
        program[2] = verb

    def solve_1(self, program: list[int]) -> int:
        self.fix_program(program, 12, 2)
        computer = IntcodeComputer(program)
        computer.run()
        return computer.memory[0]

    def solve_2(self, program: list[int]) -> int:
        for noun in range(100):
            for verb in range(100):
                self.fix_program(program, noun, verb)
                computer = IntcodeComputer(program)
                computer.run()
                if computer.memory[0] == 19690720:
                    return 100 * noun + verb
        raise ResultExpectedError
