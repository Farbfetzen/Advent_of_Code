# https://adventofcode.com/2018/day/4

import re

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2018Day04(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = self.prepare(inputs.samples[0])
        sleep_patterns = self.analyze_sleep_patterns(prepared_input)
        self.sample_results_1.append(self.solve_1(sleep_patterns))
        self.sample_results_2.append(self.solve_2(sleep_patterns))

        prepared_input = self.prepare(inputs.input)
        sleep_patterns = self.analyze_sleep_patterns(prepared_input)
        self.result_1 = self.solve_1(sleep_patterns)
        self.result_2 = self.solve_2(sleep_patterns)

    @staticmethod
    def prepare(data: str) -> list[str]:
        return sorted(data.splitlines())

    @staticmethod
    def analyze_sleep_patterns(data: list[str]):
        sleep_patterns: dict[str, list[int]] = {}
        guard = ""
        sleep_start = -1
        pattern = re.compile(r".+:(\d\d)] ([a-zA-Z# ]+(\d+)?.+)")
        for line in data:
            groups = re.match(pattern, line).groups()  # type: ignore
            minute = int(groups[0])
            activity = groups[1]
            if activity == "falls asleep":
                sleep_start = minute
            elif activity == "wakes up":
                for m in range(sleep_start, minute):
                    sleep_patterns[guard][m] += 1
            else:
                guard = groups[2]
                if guard not in sleep_patterns:
                    sleep_patterns[guard] = [0] * 60
        return sleep_patterns

    @staticmethod
    def solve_1(data: dict[str, list[int]]) -> int:
        sleepiest_guard = max(data, key=lambda k: sum(data[k]))
        minutes = data[sleepiest_guard]
        sleepiest_minute = minutes.index(max(minutes))
        return int(sleepiest_guard) * sleepiest_minute

    @staticmethod
    def solve_2(data: dict[str, list[int]]) -> int:
        best_guard = ""
        best_minute = -1
        num_asleep = -1
        for guard, minutes in data.items():
            n = max(minutes)
            if n > num_asleep:
                num_asleep = n
                best_guard = guard
                best_minute = minutes.index(n)
        return int(best_guard) * best_minute
