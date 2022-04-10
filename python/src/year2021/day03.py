# https://adventofcode.com/2021/day/3

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[str]:
    return data.splitlines()


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


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
