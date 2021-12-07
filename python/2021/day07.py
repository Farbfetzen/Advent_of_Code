# https://adventofcode.com/2021/day/7


from math import ceil, floor
from statistics import mean, median


SAMPLE_PATH = "../../input/2021-07-sample.txt"
INPUT_PATH = "../../input/2021-07-input.txt"


def get_data(filename):
    with open(filename) as file:
        return [int(x) for x in file.read().split(",")]


def part_1(positions):
    best_position = int(median(positions))
    return sum(abs(pos - best_position) for pos in positions)


def part_2(positions):
    mean_position = mean(positions)
    # Because the positions have to be ints I need to check both around the mean.
    best_positions = (floor(mean_position), ceil(mean_position))
    fuel_requirements = [0, 0]
    for i, bp in enumerate(best_positions):
        fuel = 0
        for pos in positions:
            steps = abs(pos - bp)
            fuel += steps * (steps + 1) // 2
        fuel_requirements[i] = fuel
    return int(min(fuel_requirements))


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(sample_data) == 37
    assert part_2(sample_data) == 168

    challenge_data = get_data(INPUT_PATH)
    print(part_1(challenge_data))  # 352331
    print(part_2(challenge_data))  # 99266250
