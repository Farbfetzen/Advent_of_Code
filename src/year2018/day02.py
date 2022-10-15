# https://adventofcode.com/2018/day/2

from collections import Counter

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[str]:
    return data.splitlines()


def part_1(data):
    sum_2 = 0
    sum_3 = 0
    for id_ in data:
        counter = Counter(id_)
        sum_2 += 2 in counter.values()
        sum_3 += 3 in counter.values()
    return sum_2 * sum_3


def find_ids_differing_by_1(data):
    for id_1 in data:
        for id_2 in data:
            count_differences = 0
            for a, b in zip(id_1, id_2):
                count_differences += a != b
            if count_differences == 1:
                return id_1, id_2


def part_2(data):
    id_1, id_2 = find_ids_differing_by_1(data)
    for x in enumerate(zip(id_1, id_2)):
        i = x[0]
        a, b = x[1]
        if a != b:
            return id_1[:i] + id_1[i+1:]


def solve(data: Data) -> Solution:
    challenge_data = prepare_data(data.input)
    return Solution(
        part_1=part_1(challenge_data),
        part_2=part_2(challenge_data)
    )
