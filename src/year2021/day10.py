# https://adventofcode.com/2021/day/10

from statistics import median

from src.util.types import Data, Solution


PAIRS = {")": "(", "]": "[", "}": "{", ">": "<"}
VALUES = {")": 3, "]": 57, "}": 1197, ">": 25137, "(": 1, "[": 2, "{": 3, "<": 4}


def prepare_data(data: str) -> list[str]:
    return data.splitlines()


def get_scores(data):
    part_1_score = 0
    part_2_scores = []
    for line in data:
        autocomplete_score = 0
        stack = []
        for character in line:
            if character in PAIRS:
                opening = stack.pop()
                if opening != PAIRS[character]:
                    # Line is corrupted.
                    part_1_score += VALUES[character]
                    break
            else:
                stack.append(character)
        else:
            # Line is not corrupted and therefore incomplete.
            while stack:
                autocomplete_score = autocomplete_score * 5 + VALUES[stack.pop()]
            part_2_scores.append(autocomplete_score)
    part_2_score = median(part_2_scores)
    return part_1_score, part_2_score


def solve(data: Data) -> Solution:
    sample_data = prepare_data(data.samples[0])
    sample_part_1, sample_part_2 = get_scores(sample_data)

    challenge_data = prepare_data(data.input)
    challenge_part_1, challenge_part_2 = get_scores(challenge_data)

    return Solution(
        samples_part_1=[sample_part_1],
        samples_part_2=[sample_part_2],
        part_1=challenge_part_1,
        part_2=challenge_part_2
    )
