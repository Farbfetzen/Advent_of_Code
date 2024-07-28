# https://adventofcode.com/2022/day/3

from string import ascii_letters

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[str]:
    return data.splitlines()


def sum_priorities(items: list[str]) -> int:
    return sum(ascii_letters.index(item) + 1 for item in items)


def part_1(data: list[str]) -> int:
    common_items = []
    for line in data:
        middle = len(line) // 2
        left = set(line[:middle])
        right = set(line[middle:])
        common_items.append(left.intersection(right).pop())
    return sum_priorities(common_items)


def part_2(data: list[str]) -> int:
    common_items = []
    for i in range(0, len(data), 3):
        sets = [set(rucksack) for rucksack in data[i:i+3]]
        common_items.append(set.intersection(*sets).pop())
    return sum_priorities(common_items)


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
