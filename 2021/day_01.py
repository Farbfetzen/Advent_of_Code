# https://adventofcode.com/2021/day/1


def get_data(filename):
    with open(filename) as file:
        return [int(i) for i in file.readlines()]


def part_1(depths):
    sum_increases = 0
    for i, d in enumerate(depths[1:], 1):
        previous = depths[i - 1]
        if d > previous:
            sum_increases += 1
    return sum_increases


def part_2(depths):
    return part_1([sum(w) for w in zip(depths, depths[1:], depths[2:])])


sample_data = get_data("day_01_sample.txt")
challenge_data = get_data("day_01_input.txt")

if __name__ == "__main__":
    assert part_1(sample_data) == 7
    assert part_2(sample_data) == 5

    print(part_1(challenge_data))  # 1766
    print(part_2(challenge_data))  # 1797

