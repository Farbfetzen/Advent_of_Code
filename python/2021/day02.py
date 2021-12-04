# https://adventofcode.com/2021/day/2


def get_data(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return [(direction, int(n)) for direction, n in (line.split() for line in lines)]


def follow_course(course):
    """Both parts can be done in one pass because aim in part 2 is just depth from part 1."""
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
    return horizontal_position, depth, aim


def part_1(horizontal_position, _, aim):
    return horizontal_position * aim


def part_2(horizontal_position, depth, _):
    return horizontal_position * depth


sample_data = get_data("../../input/2021-02-sample.txt")
challenge_data = get_data("../../input/2021-02-input.txt")

if __name__ == "__main__":
    hda_sample = follow_course(sample_data)
    assert part_1(*hda_sample) == 150
    assert part_2(*hda_sample) == 900

    hda_challenge = follow_course(challenge_data)
    print(part_1(*hda_challenge))  # 2073315
    print(part_2(*hda_challenge))  # 1840311528
