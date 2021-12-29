# https://adventofcode.com/2021/day/21


import functools
import itertools


SAMPLE_PATH = "../../input/2021-21-sample.txt"
INPUT_PATH = "../../input/2021-21-input.txt"


def get_data(filename):
    with open(filename) as file:
        first, second = file.read().splitlines()
    return int(first.split(": ")[1]), int(second.split(": ")[1])


def part_1(start_1, start_2):
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


@functools.cache
def count_wins(position_1, position_2, score_1, score_2):
    wins_1 = 0
    wins_2 = 0
    for roll_1, roll_2, roll_3 in itertools.product((1, 2, 3), repeat=3):
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


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(*sample_data) == 739785
    assert part_2(*sample_data) == 444356092776315

    challenge_data = get_data(INPUT_PATH)
    print(part_1(*challenge_data))  # 752247
    print(part_2(*challenge_data))  # 221109915584112
