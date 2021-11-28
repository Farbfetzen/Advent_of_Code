# https://adventofcode.com/2020/day/15


import array


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


with open("day_15_input.txt") as file:
    challenge_input = [int(x) for x in file.read().split(",")]

if __name__ == "__main__":
    print(play(challenge_input, 2020))  # 240
    print(play(challenge_input, 30_000_000))  # 505
