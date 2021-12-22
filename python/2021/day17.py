# https://adventofcode.com/2021/day/17


import re


SAMPLE_PATH = "../../input/2021-17-sample.txt"
INPUT_PATH = "../../input/2021-17-input.txt"


def get_data(filename):
    with open(filename) as file:
        return [int(x) for x in re.findall(r"-?\d+", file.read())]


def part_1(y_min):
    """The probe must return to the starting position with the starting y-velocity negated.
    In the next step it must not go further than the lowest allowed target coordinate.
    Therefore, it should be launched upwards at a speed of min_y - 1.
    So all I have to do is sum the values from 1 to min_y - 1.
    """
    return y_min * (y_min + 1) // 2


def part_2(x_min, x_max, y_min, y_max):
    """Simple brute force."""
    valid_velocities_count = 0
    for x_velocity_initial in range(x_max + 1):
        for y_velocity_initial in range(y_min, -y_min):
            x = 0
            y = 0
            x_velocity = x_velocity_initial
            y_velocity = y_velocity_initial
            while x <= x_max and y >= y_min:
                if x_min <= x and y <= y_max:
                    valid_velocities_count += 1
                    break
                x += x_velocity
                y += y_velocity
                if x_velocity > 0:
                    x_velocity -= 1
                elif x_velocity < 0:
                    x_velocity += 1
                y_velocity -= 1
    return valid_velocities_count


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(sample_data[2]) == 45
    assert part_2(*sample_data) == 112

    challenge_data = get_data(INPUT_PATH)
    print(part_1(challenge_data[2]))  # 17766
    print(part_2(*challenge_data))  # 1733
