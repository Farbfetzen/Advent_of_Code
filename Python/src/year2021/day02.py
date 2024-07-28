# https://adventofcode.com/2021/day/2

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[tuple[str, int]]:
    return [(direction, int(n)) for direction, n in (line.split() for line in data.splitlines())]


def follow_course(course):
    """Both parts can be done in one pass because aim in part 2 is just depth from part 1."""
    horizontal_position = 0
    depth = 0
    aim = 0
    for direction, n in course:
        if direction == "forward":
            horizontal_position += n
            depth += aim * n
        elif direction == "up":
            aim -= n
        elif direction == "down":
            aim += n
    return horizontal_position, depth, aim


def part_1(horizontal_position, aim):
    return horizontal_position * aim


def part_2(horizontal_position, depth):
    return horizontal_position * depth


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    horiz_pos, depth, aim = follow_course(sample_data)
    solution.samples_part_1.append(part_1(horiz_pos, aim))
    solution.samples_part_2.append(part_2(horiz_pos, depth))

    challenge_data = prepare_data(data.input)
    horiz_pos, depth, aim = follow_course(challenge_data)
    solution.part_1 = part_1(horiz_pos, aim)
    solution.part_2 = part_2(horiz_pos, depth)
    return solution
