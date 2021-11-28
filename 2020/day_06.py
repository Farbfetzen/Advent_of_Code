# https://adventofcode.com/2020/day/6


def get_data(filename):
    with open(filename) as file:
        groups = file.read().split("\n\n")
        return [[set(person) for person in group.splitlines()] for group in groups]


def part_1(groups):
    return sum(len(set.union(*group)) for group in groups)


def part_2(groups):
    return sum(len(set.intersection(*group)) for group in groups)


sample_data = get_data("day_06_sample.txt")
challenge_data = get_data("day_06_input.txt")

if __name__ == "__main__":
    assert part_1(sample_data) == 11
    assert part_2(sample_data) == 6

    print(part_1(challenge_data))  # 6686
    print(part_2(challenge_data))  # 3476
