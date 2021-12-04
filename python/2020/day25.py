# https://adventofcode.com/2020/day/25

# No part 2 on the 25th.


def get_data(filename):
    with open(filename) as file:
        return [int(x) for x in file.read().splitlines()]


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


sample_data = get_data("../../input/2020-25-sample.txt")
challenge_data = get_data("../../input/2020-25-input.txt")

if __name__ == "__main__":
    assert part_1(sample_data) == 14897079

    print(part_1(challenge_data))  # 16902792
