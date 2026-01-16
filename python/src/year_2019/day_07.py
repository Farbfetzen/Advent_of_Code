# https://adventofcode.com/2019/day/7

import itertools

from src.util.inputs import Inputs
from src.util.solution import Solution
from src.year_2019.intcode import IntcodeComputer


class Solution2019Day07(Solution):

    def solve(self, inputs: Inputs) -> None:
        for i, sample in enumerate(inputs.samples):
            if i < 3:
                self.sample_results_1.append(self.solve_1(sample))
            else:
                self.sample_results_2.append(self.solve_2(sample))

        self.result_1 = self.solve_1(inputs.input)
        self.result_2 = self.solve_2(inputs.input)

    def solve_1(self, program: str) -> int:
        return self.test_phase_settings(range(5), program)

    def solve_2(self, program: str) -> int:
        return self.test_phase_settings(range(5, 10), program)

    @staticmethod
    def test_phase_settings(phase_settings_range: range, program: str) -> int:
        max_signal = 0
        for phase_settings in itertools.permutations(phase_settings_range):
            signal = 0
            amplifiers = [IntcodeComputer(program) for _ in phase_settings]
            for i, amp in enumerate(amplifiers):
                signal = amp.run(phase_settings[i], signal)[0]
            while not amplifiers[0].halted:
                for amp in amplifiers:
                    signal = amp.run(signal)[0]
            max_signal = max(signal, max_signal)
        return max_signal
