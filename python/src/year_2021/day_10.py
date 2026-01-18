# https://adventofcode.com/2021/day/10

from statistics import median

from src.util.inputs import Inputs
from src.util.solution import Solution


PAIRS = {")": "(", "]": "[", "}": "{", ">": "<"}
VALUES = {")": 3, "]": 57, "}": 1197, ">": 25137, "(": 1, "[": 2, "{": 3, "<": 4}


class Solution2021Day10(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = inputs.samples[0].splitlines()
        score_1, score_2 = self.get_scores(prepared_input)
        self.sample_results_1.append(score_1)
        self.sample_results_2.append(score_2)

        prepared_input = inputs.input.splitlines()
        self.result_1, self.result_2 = self.get_scores(prepared_input)

    @staticmethod
    def get_scores(data: list[str]) -> tuple[int, int]:
        part_1_score = 0
        part_2_scores = []
        for line in data:
            autocomplete_score = 0
            stack: list[str] = []
            for character in line:
                if character in PAIRS:
                    opening = stack.pop()
                    if opening != PAIRS[character]:
                        # Line is corrupted.
                        part_1_score += VALUES[character]
                        break
                else:
                    stack.append(character)
            else:
                # Line is not corrupted and therefore incomplete.
                while stack:
                    autocomplete_score = autocomplete_score * 5 + VALUES[stack.pop()]
                part_2_scores.append(autocomplete_score)
        part_2_score = int(median(part_2_scores))
        return part_1_score, part_2_score
