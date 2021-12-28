# https://adventofcode.com/2021/day/21


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


# def part_2(foo):
#     pass


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(*sample_data) == 739785
    # assert part_2(*sample_data) ==

    challenge_data = get_data(INPUT_PATH)
    print(part_1(*challenge_data))  # 752247
    # print(part_2(*challenge_data))  #
