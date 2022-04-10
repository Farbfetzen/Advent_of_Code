# https://adventofcode.com/2021/day/17

from itertools import product
from re import findall

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[int]:
    return [int(x) for x in findall(r"-?\d+", data)]


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
    for x_velocity_initial, y_velocity_initial in product(range(x_max + 1), range(y_min, -y_min)):
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


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data[2]))
    solution.samples_part_2.append(part_2(*sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data[2])
    solution.part_2 = part_2(*challenge_data)
    return solution
