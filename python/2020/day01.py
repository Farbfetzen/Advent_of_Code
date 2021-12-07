# https://adventofcode.com/2020/day/1


SAMPLE_PATH = "../../input/2020-01-sample.txt"
INPUT_PATH = "../../input/2020-01-input.txt"


def get_data(filename):
    with open(filename) as file:
        return [int(i) for i in file.read().splitlines()]


def part_1(expenses):
    # Add numbers to the set after checking to avoid possible error
    # if the data contains 1010.
    seen = set()
    for x in expenses:
        y = 2020 - x
        if y in seen:
            return x * y
        seen.add(x)


def part_2(expenses):
    seen = set()
    for i, x in enumerate(expenses):
        for j, y in enumerate(expenses[(i + 1):]):
            z = 2020 - x - y
            if z in seen:
                return x * y * z
            seen.add(x)
            seen.add(y)


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(sample_data) == 514579
    assert part_2(sample_data) == 241861950

    challenge_data = get_data(INPUT_PATH)
    print(part_1(challenge_data))  # 436404
    print(part_2(challenge_data))  # 274879808
