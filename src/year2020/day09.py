# https://adventofcode.com/2020/day/9

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[int]:
    return [int(i) for i in data.splitlines()]


def valid(preamble, n):
    for i, a in enumerate(preamble[:-1]):
        for b in preamble[(i + 1):]:
            if a + b == n:
                return True
    return False


def part_1(numbers, pre_len):
    for i, n in enumerate(numbers[pre_len:]):
        if not valid(numbers[i:(pre_len + i)], n):
            return n


def part_2(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 2, len(numbers)):
            numbers_slice = numbers[i:j]
            sum_ = sum(numbers_slice)
            if sum_ == target:
                return min(numbers_slice) + max(numbers_slice)
            if sum_ > target:
                break


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    sample_invalid_number = part_1(sample_data, 5)
    solution.samples_part_1.append(sample_invalid_number)
    solution.samples_part_2.append(part_2(sample_data, sample_invalid_number))

    challenge_data = prepare_data(data.input)
    invalid_number = part_1(challenge_data, 25)
    solution.part_1 = invalid_number
    solution.part_2 = part_2(challenge_data, invalid_number)
    return solution
