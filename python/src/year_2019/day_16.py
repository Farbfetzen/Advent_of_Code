# https://adventofcode.com/2019/day/16

import itertools

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2019Day16(Solution):

    def solve(self, inputs: Inputs) -> None:
        for i, sample in enumerate(inputs.samples):
            signal = self.prepare(sample)
            if i < 3:
                self.sample_results_1.append(self.solve_1(signal))
            else:
                self.sample_results_2.append(self.solve_2(signal))

        signal = self.prepare(inputs.input)
        self.result_1 = self.solve_1(signal)
        self.result_2 = self.solve_2(signal)

    @staticmethod
    def prepare(data: str) -> list[int]:
        return [int(x) for x in data]

    @staticmethod
    def solve_1(signal: list[int]) -> str:
        base_pattern = (0, 1, 0, -1)
        length = len(signal)
        patterns = []
        for i in range(1, length + 1):
            pattern = itertools.cycle(itertools.chain.from_iterable(itertools.repeat(x, i) for x in base_pattern))
            next(pattern)
            patterns.append(tuple(itertools.islice(pattern, length)))
        for _ in range(100):
            output = [0] * length
            for i, pattern_ in enumerate(patterns):
                n = sum(x * pattern_[j] for j, x in enumerate(signal))
                output[i] = abs(n) % 10
            signal = output
        return "".join(str(x) for x in signal[:8])

    @staticmethod
    def solve_2(signal: list[int]) -> str:
        # Took me a long time, but then I saw the light with the help of this thread:
        # https://www.reddit.com/r/adventofcode/comments/ebf5cy/2019_day_16_part_2_understanding_how_to_come_up
        offset = int("".join(str(x) for x in signal[:7]))
        # Only works if the message is in the second half of the signal.
        assert offset >= len(signal) * 5_000
        signal = list(itertools.islice(itertools.chain.from_iterable(itertools.repeat(signal, 10_000)), offset, None))
        signal.reverse()
        for _ in range(100):
            signal = [x % 10 for x in itertools.accumulate(signal)]
        return "".join(str(x) for x in signal[-1:-9:-1])
