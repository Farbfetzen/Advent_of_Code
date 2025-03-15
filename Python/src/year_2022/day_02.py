# https://adventofcode.com/2022/day/2

from src.util.inputs import Inputs
from src.util.solution import Solution


POINTS_LOSS = 0
POINTS_DRAW = 3
POINTS_WIN = 6
POINTS_CHOICES = {"A": 1, "B": 2, "C": 3}


class Solution2022Day02(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(prepared_input))
        self.sample_results_2.append(self.solve_2(prepared_input))

        prepared_input = self.prepare(inputs.input)
        self.result_1 = self.solve_1(prepared_input)
        self.result_2 = self.solve_2(prepared_input)

    @staticmethod
    def prepare(data: str) -> list[list[str]]:
        return [line.split() for line in data.split("\n")]

    @staticmethod
    def solve_1(rounds: list[list[str]]) -> int:
        xyz_to_abc = {"X": "A", "Y": "B", "Z": "C"}
        total_points = 0
        for left, right in rounds:
            points_left = POINTS_CHOICES[left]
            points_right = POINTS_CHOICES[xyz_to_abc[right]]
            total_points += points_right
            if points_left == points_right:
                total_points += POINTS_DRAW
            elif points_left == points_right % 3 + 1:
                total_points += POINTS_LOSS
            else:
                total_points += POINTS_WIN
        return total_points

    @staticmethod
    def solve_2(rounds: list[list[str]]) -> int:
        total_points = 0
        for left, right in rounds:
            points_left = POINTS_CHOICES[left]
            if right == "X":
                total_points += POINTS_LOSS + (points_left - 2) % 3 + 1
            elif right == "Y":
                total_points += POINTS_DRAW + points_left
            else:
                total_points += POINTS_WIN + points_left % 3 + 1
        return total_points
