# https://adventofcode.com/2021/day/3


def get_data(filename):
    with open(filename) as file:
        return file.read().splitlines()


def count_bits(numbers):
    return [sum(int(b) for b in bits) for bits in list(zip(*numbers))]


def get_rating(numbers, search_most_common=True):
    numbers = numbers.copy()
    i = 0
    while len(numbers) > 1:
        counts = count_bits(numbers)
        desired_bit = counts[i] < len(numbers) / 2
        if search_most_common:
            desired_bit = not desired_bit
        desired_bit = str(int(desired_bit))
        numbers = [n for n in numbers if n[i] == desired_bit]
        i += 1
    return int(numbers[0], 2)


def part_1(report):
    sums = count_bits(report)
    most_common_1 = [x > len(report) / 2 for x in sums]
    gamma_rate = "".join(str(int(x)) for x in most_common_1)
    epsilon_rate = "".join(str(int(not x)) for x in most_common_1)
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part_2(report):
    oxygen_generator_rating = get_rating(report, True)
    co2_scrubber_rating = get_rating(report, False)
    return oxygen_generator_rating * co2_scrubber_rating


sample_data = get_data("day_03_sample.txt")
challenge_data = get_data("day_03_input.txt")

if __name__ == "__main__":
    assert part_1(sample_data) == 198
    assert part_2(sample_data) == 230

    print(part_1(challenge_data))  # 693486
    print(part_2(challenge_data))  # 3379326
