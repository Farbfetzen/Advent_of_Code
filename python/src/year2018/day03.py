# https://adventofcode.com/2018/day/3

import collections
import re

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[str]:
    return data.splitlines()


def get_claims(data):
    claims = []
    pattern = re.compile(r"(\d+)")
    for line in data:
        claim = []
        for s in pattern.split(line):
            if s.isdigit():
                claim.append(int(s))
        claims.append(claim)
    return claims


def part_1_and_2(data):
    all_coordinates = {}
    all_coordinates_list = []
    id_ = None
    for claim in get_claims(data):
        id_, left, top, width, height = claim
        claim_xy = []
        for x in range(left+1, left+width+1):
            for y in range(top+1, top+height+1):
                claim_xy.append(str(x)+" "+str(y))
        all_coordinates[id_] = claim_xy
        all_coordinates_list += claim_xy

    counter_1 = collections.Counter(all_coordinates_list)
    counter_2 = collections.Counter(counter_1.values())
    if 1 in counter_2:
        del counter_2[1]

    unique = {k for k, v in counter_1.items() if v == 1}
    for id_, claim in all_coordinates.items():
        if set(claim).issubset(unique):
            break
    return sum(counter_2.values()), id_


def solve(data: Data) -> Solution:
    challenge_data = prepare_data(data.input)
    solution_part_1, solution_part_2 = part_1_and_2(challenge_data)
    return Solution(
        part_1=solution_part_1,
        part_2=solution_part_2
    )
