# https://adventofcode.com/2019/day/21

from src.util.inputs import Inputs
from src.util.solution import Solution
from src.year_2019.intcode import IntcodeComputer


class Solution2019Day21(Solution):
    # Jump if there is a hole at A or B or C but only if there is ground at D.
    common_script_part = "\n".join(("NOT B J", "NOT C T", "OR T J", "NOT A T", "OR T J", "AND D J", ""))

    def solve(self, inputs: Inputs) -> None:
        self.solve_1(inputs.input)
        self.solve_2(inputs.input)

    def solve_1(self, program: str) -> None:
        springscript = self.common_script_part + "WALK\n"
        self.result_1 = self.survey(program, springscript)

    def solve_2(self, program: str) -> None:
        # Same as in part 1 but there must also be ground at H.
        springscript = self.common_script_part + "OR H T\n" + "AND T J\n" + "RUN\n"
        self.result_2 = self.survey(program, springscript)

    @staticmethod
    def survey(program: str, script: str) -> int:
        droid = IntcodeComputer(program)
        _words = droid.run_ascii()[0]
        # print(_words)  # prints "Input instructions:"
        _words, damage = droid.run_ascii(script)
        # print(_words)  # prints "Walking..." in part 1 and "Running..." in part 2.
        assert isinstance(damage, int)
        return damage
