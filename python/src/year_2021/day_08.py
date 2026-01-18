# https://adventofcode.com/2021/day/8

from src.util.inputs import Inputs
from src.util.solution import Solution


LENGTH_TO_DIGIT = {
    2: (1,),
    3: (7,),
    4: (4,),
    5: (2, 3, 5),
    6: (0, 6, 9),
    7: (8,),
}


class Solution2021Day08(Solution):

    def solve(self, inputs: Inputs) -> None:
        patterns, outputs = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(outputs))
        self.sample_results_2.append(self.solve_2(patterns, outputs))

        patterns, outputs = self.prepare(inputs.input)
        self.result_1 = self.solve_1(outputs)
        self.result_2 = self.solve_2(patterns, outputs)

    @staticmethod
    def prepare(data: str) -> tuple[list[list[frozenset[str]]], list[list[frozenset[str]]]]:
        all_patterns = []
        all_outputs = []
        for line in data.splitlines():
            patterns, outputs = line.split("|")
            all_patterns.append([frozenset(pattern) for pattern in patterns.split()])
            all_outputs.append([frozenset(output) for output in outputs.split()])
        return all_patterns, all_outputs

    @staticmethod
    def solve_1(all_outputs: list[list[frozenset[str]]]) -> int:
        unique_lengths = {2, 3, 4, 7}
        result = 0
        for outputs in all_outputs:
            for signals in outputs:
                if len(signals) in unique_lengths:
                    result += 1
        return result

    def solve_2(self, all_patterns: list[list[frozenset[str]]], all_outputs: list[list[frozenset[str]]]) -> int:
        result = 0
        for patterns, outputs in zip(all_patterns, all_outputs):
            pattern_to_numbers = self.determine_mapping(patterns)
            for i, magnitude in enumerate((1000, 100, 10, 1)):
                result += pattern_to_numbers[outputs[i]] * magnitude
        return result

    @staticmethod
    def determine_mapping(patterns: list[frozenset[str]]) -> dict[frozenset[str], int]:
        candidates: list[list[frozenset[str]]] = [[] for _ in range(10)]
        for pattern in patterns:
            for digit in LENGTH_TO_DIGIT[len(pattern)]:
                candidates[digit].append(pattern)

        # 1 and 4 have unique numbers of segments.
        d1 = candidates[1][0]
        d4 = candidates[4][0]

        # 2, 5, and 6 must not contain both segments of 1.
        for i in (2, 5, 6):
            candidates[i] = [c for c in candidates[i] if not d1.issubset(c)]

        # The intersection of 5 and 4 must have length 3.
        candidates[5] = [c for c in candidates[5] if len(d4.intersection(c)) == 3]

        # The intersection of 2 and 4 must have length 2.
        candidates[2] = [c for c in candidates[2] if len(d4.intersection(c)) == 2]

        # The intersection of 9 and 4 must have length 4.
        candidates[9] = [c for c in candidates[9] if len(d4.intersection(c)) == 4]

        # The intersection of 3 and 1 must have length 2.
        candidates[3] = [c for c in candidates[3] if len(d1.intersection(c)) == 2]

        # The intersection of 0 and 1 must have length 2 and between 0 and 4 is must have length 3.
        candidates[0] = [c for c in candidates[0] if len(d1.intersection(c)) == 2 and len(d4.intersection(c)) == 3]

        assert all(len(c) == 1 for c in candidates)
        return {c[0]: i for i, c in enumerate(candidates)}
