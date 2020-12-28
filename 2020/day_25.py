# https://adventofcode.com/2020/day/25


def part_1(public_keys):
    value = 1
    found = 0
    loop_sizes = [0, 0]
    i = 0
    while True:
        i += 1
        value = (value * 7) % 20201227
        if value in public_keys:
            loop_sizes[public_keys.index(value)] = i
            found += 1
        if found == 2:
            break

    loop_size = min(loop_sizes)  # Save time by using the smaller loop size.
    public_key = public_keys[loop_sizes.index(max(loop_sizes))]
    value = 1
    for _ in range(loop_size):
        value = (value * public_key) % 20201227
    return value


test_input = """\
5764801
17807724
""".splitlines()
test_input = (int(test_input[0]), int(test_input[1]))
assert part_1(test_input) == 14897079

with open("day_25_input.txt") as file:
    challenge_input = file.read().splitlines()
challenge_input = (int(challenge_input[0]), int(challenge_input[1]))
print(part_1(challenge_input))  # 16902792
