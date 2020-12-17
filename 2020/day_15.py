# https://adventofcode.com/2020/day/15


import array


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
    print(f"Output for {numbers} on turn {turn} = {last_num}.")
    return last_num


assert play((0, 3, 6), 2020) == 436
assert play((1, 3, 2), 2020) == 1
assert play((2, 1, 3), 2020) == 10
assert play((1, 2, 3), 2020) == 27
assert play((2, 3, 1), 2020) == 78
assert play((3, 2, 1), 2020) == 438
assert play((3, 1, 2), 2020) == 1836

assert play((0, 3, 6), 30_000_000) == 175594
assert play((1, 3, 2), 30_000_000) == 2578
assert play((2, 1, 3), 30_000_000) == 3544142
assert play((1, 2, 3), 30_000_000) == 261214
assert play((2, 3, 1), 30_000_000) == 6895259
assert play((3, 2, 1), 30_000_000) == 18
assert play((3, 1, 2), 30_000_000) == 362


with open("day_15_input.txt") as file:
    challenge_input = [int(x) for x in file.read().split(",")]
print(play(challenge_input, 2020))  # 240
print(play(challenge_input, 30_000_000))  # 505
