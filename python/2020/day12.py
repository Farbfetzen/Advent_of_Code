# https://adventofcode.com/2020/day/12


import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from pygame import Vector2


SAMPLE_PATH = "../../input/2020-12-sample.txt"
INPUT_PATH = "../../input/2020-12-input.txt"


def get_data(filename):
    with open(filename) as file:
        return file.read().splitlines()


def navigate(instructions, part=1):
    position = Vector2(0, 0)
    # "direction_or_waypoint" is either the ship direction in part 1
    # or the waypoint position relative to the ship in part 2.
    direction_or_waypoint = Vector2(1, 0) if part == 1 else Vector2(10, -1)
    # IMPORTANT: This uses coordinates where y increases downwards,
    # which also inverts the rotations!
    cardinal_directions = {
        "N": Vector2(0, -1),
        "S": Vector2(0, 1),
        "W": Vector2(-1, 0),
        "E": Vector2(1, 0),
    }
    for instr in instructions:
        action = instr[0]
        value = int(instr[1:])
        if action in cardinal_directions:
            if part == 1:
                position += cardinal_directions[action] * value
            else:
                direction_or_waypoint += cardinal_directions[action] * value
        elif action == "L":
            direction_or_waypoint.rotate_ip(-value)
        elif action == "R":
            direction_or_waypoint.rotate_ip(value)
        elif action == "F":
            position += direction_or_waypoint * value
    return int(abs(position.x) + abs(position.y))


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert navigate(sample_data, part=1) == 25
    assert navigate(sample_data, part=2) == 286

    challenge_data = get_data(INPUT_PATH)
    print(navigate(challenge_data, part=1))  # 362
    print(navigate(challenge_data, part=2))  # 29895
