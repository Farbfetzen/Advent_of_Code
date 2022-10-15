# https://adventofcode.com/2021/day/6

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[int]:
    return [int(x) for x in data.split(",")]


def simulate(fish_ages):
    count = [fish_ages.count(i) for i in range(9)]
    result_at_day_80 = 0
    for day in range(1, 256+1):
        zeros = count[0]
        count[:-1] = count[1:]
        count[6] += zeros
        count[8] = zeros
        if day == 80:
            result_at_day_80 = sum(count)
    return result_at_day_80, sum(count)


def solve(data: Data) -> Solution:
    sample_data = prepare_data(data.samples[0])
    sample_part_1, sample_part_2 = simulate(sample_data)

    challenge_data = prepare_data(data.input)
    challenge_part_1, challenge_part_2 = simulate(challenge_data)

    return Solution(
        samples_part_1=[sample_part_1],
        samples_part_2=[sample_part_2],
        part_1=challenge_part_1,
        part_2=challenge_part_2
    )
