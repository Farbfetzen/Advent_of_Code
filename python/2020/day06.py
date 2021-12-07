# https://adventofcode.com/2020/day/6


SAMPLE_PATH = "../../input/2020-06-sample.txt"
INPUT_PATH = "../../input/2020-06-input.txt"


def get_data(filename):
    with open(filename) as file:
        groups = file.read().split("\n\n")
        return [[set(person) for person in group.splitlines()] for group in groups]


def part_1(groups):
    return sum(len(set.union(*group)) for group in groups)


def part_2(groups):
    return sum(len(set.intersection(*group)) for group in groups)


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(sample_data) == 11
    assert part_2(sample_data) == 6

    challenge_data = get_data(INPUT_PATH)
    print(part_1(challenge_data))  # 6686
    print(part_2(challenge_data))  # 3476
