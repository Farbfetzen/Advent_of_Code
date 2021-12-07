# https://adventofcode.com/2021/day/7


from math import inf
from statistics import median


SAMPLE_PATH = "../../input/2021-07-sample.txt"
INPUT_PATH = "../../input/2021-07-input.txt"


def get_data(filename):
    with open(filename) as file:
        return [int(x) for x in file.read().split(",")]


def part_1(positions):
    best_position = int(median(positions))
    return sum(abs(pos - best_position) for pos in positions)


def calc_fuel(steps):
    return steps * (steps + 1) // 2


def part_2(positions):
    """Just a simple search from min to max position. I could improve it but this one
    is fast enough. There should be only one minimum so no need to search the other
    positions after it is found.
    """
    min_fuel = inf
    for best_pos in range(min(positions), max(positions) + 1):
        fuel = sum(calc_fuel(abs(pos - best_pos)) for pos in positions)
        if fuel >= min_fuel:
            return min_fuel
        min_fuel = fuel


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(sample_data) == 37
    assert part_2(sample_data) == 168

    challenge_data = get_data(INPUT_PATH)
    print(part_1(challenge_data))  # 352331
    print(part_2(challenge_data))  # 99266250
