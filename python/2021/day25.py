# https://adventofcode.com/2021/day/25


SAMPLE_PATH = "../../input/2021-25-sample.txt"
INPUT_PATH = "../../input/2021-25-input.txt"


def get_data(filename):
    with open(filename) as file:
        data = file.read().splitlines()
    cucumbers_right = set()
    cucumbers_down = set()
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == ">":
                cucumbers_right.add((x, y))
            elif char == "v":
                cucumbers_down.add((x, y))
    width = len(data[0])
    height = len(data)
    return cucumbers_right, cucumbers_down, width, height


def part_1(cucumbers_right, cucumbers_down, width, height):
    steps = 0
    while True:
        steps += 1
        move_right = []
        for x, y in cucumbers_right:
            new_position = ((x + 1) % width, y)
            if new_position not in cucumbers_right and new_position not in cucumbers_down:
                move_right.append(((x, y), new_position))
        for position, new_position in move_right:
            cucumbers_right.remove(position)
            cucumbers_right.add(new_position)
        move_down = []
        for x, y in cucumbers_down:
            new_position = (x, (y + 1) % height)
            if new_position not in cucumbers_down and new_position not in cucumbers_right:
                move_down.append(((x, y), new_position))
        for position, new_position in move_down:
            cucumbers_down.remove(position)
            cucumbers_down.add(new_position)
        if not move_right and not move_down:
            return steps


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(*sample_data) == 58

    challenge_data = get_data(INPUT_PATH)
    print(part_1(*challenge_data))  # 532
    print("No part 2 on day 25. Merry Christmas!")
