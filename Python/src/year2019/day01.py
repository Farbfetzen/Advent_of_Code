# https://adventofcode.com/2019/day/1

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[int]:
    return [int(i) for i in data.splitlines()]


def calculate_fuel(mass: int) -> int:
    return max(mass // 3 - 2, 0)


def part_1(masses: list[int]) -> int:
    return sum(calculate_fuel(m) for m in masses)


def part_2(masses: list[int]) -> int:
    total = 0
    for m in masses:
        additional_fuel = calculate_fuel(m)
        while additional_fuel > 0:
            total += additional_fuel
            additional_fuel = calculate_fuel(additional_fuel)
    return total


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
