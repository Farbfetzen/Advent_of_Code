# https://adventofcode.com/2020/day/15


import array


INPUT_PATH = "../../input/2020-15-input.txt"


def get_data(filename):
    with open(filename) as file:
        return [int(x) for x in file.read().split(",")]


# noinspection PyUnboundLocalVariable
def play(numbers, end_turn):
    # Using an array of unsigned ints gives a small speed boost.
    memory = array.array("I", [0] * end_turn)
    for turn, last_num in enumerate(numbers, start=1):
        last_seen = memory[last_num]
        memory[last_num] = turn
    for turn in range(turn+1, end_turn+1):
        if last_seen > 0:
            last_num = turn - last_seen - 1
        else:
            last_num = 0
        last_seen = memory[last_num]
        memory[last_num] = turn
    return last_num


if __name__ == "__main__":
    challenge_data = get_data(INPUT_PATH)
    print(play(challenge_data, 2020))  # 240
    print(play(challenge_data, 30_000_000))  # 505
