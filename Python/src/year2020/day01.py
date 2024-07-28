# https://adventofcode.com/2020/day/1

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[int]:
    return [int(i) for i in data.splitlines()]


def part_1(expenses):
    # Add numbers to the set after checking to avoid possible error
    # if the data contains 1010.
    seen = set()
    for x in expenses:
        y = 2020 - x
        if y in seen:
            return x * y
        seen.add(x)


def part_2(expenses):
    seen = set()
    for i, x in enumerate(expenses):
        for j, y in enumerate(expenses[(i + 1):]):
            z = 2020 - x - y
            if z in seen:
                return x * y * z
            seen.add(x)
            seen.add(y)


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
