# https://adventofcode.com/2018/day/1

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[int]:
    return [int(line) for line in data.splitlines()]


def part_1(data):
    return sum(data)  # 561


def part_2(data):
    frequency = 0
    seen = set()
    while True:
        for change in data:
            if frequency in seen:
                return frequency
            seen.add(frequency)
            frequency += change


def solve(data: Data) -> Solution:
    challenge_data = prepare_data(data.input)
    return Solution(
        part_1=part_1(challenge_data),
        part_2=part_2(challenge_data)
    )
