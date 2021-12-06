# https://adventofcode.com/2019/day/1


def get_data(filename):
    with open(filename) as file:
        return [int(i) for i in file.read().splitlines()]


def calculate_fuel(mass):
    return max(mass // 3 - 2, 0)


def part_1(masses):
    return sum(calculate_fuel(m) for m in masses)


def part_2(masses):
    total = 0
    for m in masses:
        additional_fuel = calculate_fuel(m)
        while additional_fuel > 0:
            total += additional_fuel
            additional_fuel = calculate_fuel(additional_fuel)
    return total


sample_data = get_data("../../input/2019-01-sample.txt")
challenge_data = get_data("../../input/2019-01-input.txt")

if __name__ == "__main__":
    assert part_1(sample_data) == 34241
    assert part_2(sample_data) == 51316

    print(part_1(challenge_data))  # 3223398
    print(part_2(challenge_data))  # 4832253
