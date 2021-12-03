# https://adventofcode.com/2021/day/1


def get_data(filename):
    with open(filename) as file:
        return [int(i) for i in file.read().splitlines()]


def part_1(depths):
    return sum(x < y for x, y in zip(depths, depths[1:]))


def part_2(depths):
    # Shortcut: I only need to compare the values that are 3 steps apart because
    # a + b + c < b + c + d can be canceled down to a < d.
    return sum(x < y for x, y in zip(depths, depths[3:]))


sample_data = get_data("day_01_sample.txt")
challenge_data = get_data("day_01_input.txt")

if __name__ == "__main__":
    assert part_1(sample_data) == 7
    assert part_2(sample_data) == 5

    print(part_1(challenge_data))  # 1766
    print(part_2(challenge_data))  # 1797

