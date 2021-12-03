# https://adventofcode.com/2021/day/2


def get_data(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return [(direction, int(n)) for direction, n in (line.split() for line in lines)]


def part_1(course):
    horizontal_position = 0
    depth = 0
    for direction, n in course:
        if direction == "forward":
            horizontal_position += n
        elif direction == "up":
            depth -= n
        elif direction == "down":
            depth += n
    return horizontal_position * depth


def part_2(course):
    horizontal_position = 0
    depth = 0
    aim = 0
    for direction, n in course:
        if direction == "forward":
            horizontal_position += n
            depth += aim * n
        elif direction == "up":
            aim -= n
        elif direction == "down":
            aim += n
    return horizontal_position * depth


sample_data = get_data("day_02_sample.txt")
challenge_data = get_data("day_02_input.txt")

if __name__ == "__main__":
    assert part_1(sample_data) == 150
    assert part_2(sample_data) == 900

    print(part_1(challenge_data))  # 2073315
    print(part_2(challenge_data))  # 1840311528
