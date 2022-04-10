# https://adventofcode.com/2021/day/21

from functools import cache
from itertools import cycle, product

from src.util.types import Data, Solution


def prepare_data(data: str) -> tuple[int, int]:
    first, second = data.splitlines()
    return int(first.split(": ")[1]), int(second.split(": ")[1])


def part_1(start_1, start_2):
    positions = [start_1, start_2]
    scores = [0, 0]
    player_index = 0
    die = cycle(range(1, 101))
    times_rolled = 0
    while scores[0] < 1000 and scores[1] < 1000:
        roll = next(die) + next(die) + next(die)
        times_rolled += 3
        positions[player_index] = (positions[player_index] - 1 + roll) % 10 + 1
        scores[player_index] += positions[player_index]
        player_index = not player_index
    return scores[player_index] * times_rolled


@cache
def count_wins(position_1, position_2, score_1, score_2):
    wins_1 = 0
    wins_2 = 0
    for roll_1, roll_2, roll_3 in product((1, 2, 3), repeat=3):
        new_position_1 = (position_1 - 1 + roll_1 + roll_2 + roll_3) % 10 + 1
        new_score_1 = score_1 + new_position_1
        if new_score_1 >= 21:
            wins_1 += 1
        else:
            new_wins_2, new_wins_1 = count_wins(position_2, new_position_1, score_2, new_score_1)
            wins_1 += new_wins_1
            wins_2 += new_wins_2
    return wins_1, wins_2


def part_2(start_1, start_2):
    scores = count_wins(start_1, start_2, 0, 0)
    return max(scores)


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(*sample_data))
    solution.samples_part_2.append(part_2(*sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(*challenge_data)
    solution.part_2 = part_2(*challenge_data)
    return solution
