# https://adventofcode.com/2021/day/21

import itertools
from functools import cache

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2021Day21(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(*prepared_input))
        self.sample_results_2.append(self.solve_2(*prepared_input))

        prepared_input = self.prepare(inputs.input)
        self.result_1 = self.solve_1(*prepared_input)
        self.result_2 = self.solve_2(*prepared_input)

    @staticmethod
    def prepare(data: str) -> tuple[int, int]:
        first, second = data.splitlines()
        return int(first.split(": ")[1]), int(second.split(": ")[1])

    @staticmethod
    def solve_1(start_1: int, start_2: int) -> int:
        positions = [start_1, start_2]
        scores = [0, 0]
        player_index = 0
        die = itertools.cycle(range(1, 101))
        times_rolled = 0
        while scores[0] < 1000 and scores[1] < 1000:
            roll = next(die) + next(die) + next(die)
            times_rolled += 3
            positions[player_index] = (positions[player_index] - 1 + roll) % 10 + 1
            scores[player_index] += positions[player_index]
            player_index = not player_index
        return scores[player_index] * times_rolled

    def solve_2(self, start_1: int, start_2: int) -> int:
        scores = self.count_wins(start_1, start_2, 0, 0)
        return max(scores)

    @cache
    def count_wins(self, position_1: int, position_2: int, score_1: int, score_2: int) -> tuple[int, int]:
        wins_1 = 0
        wins_2 = 0
        for roll_1, roll_2, roll_3 in itertools.product((1, 2, 3), repeat=3):
            new_position_1 = (position_1 - 1 + roll_1 + roll_2 + roll_3) % 10 + 1
            new_score_1 = score_1 + new_position_1
            if new_score_1 >= 21:
                wins_1 += 1
            else:
                new_wins_2, new_wins_1 = self.count_wins(position_2, new_position_1, score_2, new_score_1)
                wins_1 += new_wins_1
                wins_2 += new_wins_2
        return wins_1, wins_2
