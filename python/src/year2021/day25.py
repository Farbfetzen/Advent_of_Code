# https://adventofcode.com/2021/day/25

from src.util.types import Data, Point2, Solution


def prepare_data(data: str) -> tuple[set[Point2], set[Point2], int, int]:
    data_list = data.splitlines()
    cucumbers_right = set()
    cucumbers_down = set()
    for y, row in enumerate(data_list):
        for x, char in enumerate(row):
            if char == ">":
                cucumbers_right.add(Point2(x, y))
            elif char == "v":
                cucumbers_down.add(Point2(x, y))
    width = len(data_list[0])
    height = len(data_list)
    return cucumbers_right, cucumbers_down, width, height


def part_1(cucumbers_right, cucumbers_down, width, height):
    steps = 0
    while True:
        steps += 1
        move_right = []
        for x, y in cucumbers_right:
            new_position = Point2((x + 1) % width, y)
            if new_position not in cucumbers_right and new_position not in cucumbers_down:
                move_right.append((Point2(x, y), new_position))
        for position, new_position in move_right:
            cucumbers_right.remove(position)
            cucumbers_right.add(new_position)
        move_down = []
        for x, y in cucumbers_down:
            new_position = Point2(x, (y + 1) % height)
            if new_position not in cucumbers_down and new_position not in cucumbers_right:
                move_down.append(((x, y), new_position))
        for position, new_position in move_down:
            cucumbers_down.remove(position)
            cucumbers_down.add(new_position)
        if not move_right and not move_down:
            return steps


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(*sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(*challenge_data)
    solution.part_2 = "No part 2 on day 25. Merry Christmas!"
    return solution
