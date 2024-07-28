# https://adventofcode.com/2022/day/2

from src.util.types import Data, Solution


POINTS_LOSS = 0
POINTS_DRAW = 3
POINTS_WIN = 6
POINTS_CHOICES = {"A": 1, "B": 2, "C": 3}


def prepare_data(data: str) -> list[list[str]]:
    return [line.split() for line in data.split("\n")]


def part_1(rounds: list[list[str]]) -> int:
    xyz_to_abc = {"X": "A", "Y": "B", "Z": "C"}
    total_points = 0
    for left, right in rounds:
        points_left = POINTS_CHOICES[left]
        points_right = POINTS_CHOICES[xyz_to_abc[right]]
        total_points += points_right
        if points_left == points_right:
            total_points += POINTS_DRAW
        elif points_left == points_right % 3 + 1:
            total_points += POINTS_LOSS
        else:
            total_points += POINTS_WIN
    return total_points


def part_2(rounds: list[list[str]]) -> int:
    total_points = 0
    for left, right in rounds:
        points_left = POINTS_CHOICES[left]
        if right == "X":
            total_points += POINTS_LOSS + (points_left - 2) % 3 + 1
        elif right == "Y":
            total_points += POINTS_DRAW + points_left
        else:
            total_points += POINTS_WIN + points_left % 3 + 1
    return total_points


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
