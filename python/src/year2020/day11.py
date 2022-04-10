# https://adventofcode.com/2020/day/11

# TODO: Improve the performance of both parts.

import numpy

from src.util.types import Data, Solution


def prepare_data(data: str) -> numpy.ndarray:
    return numpy.array([list(line) for line in data.splitlines()])


def part_1(seats):
    height, width = seats.shape
    while True:
        new_seats = seats.copy()
        for y, row in enumerate(seats):
            for x, char in enumerate(row):
                if char == ".":
                    continue
                neighborhood = seats[
                    max(y-1, 0):min(y+2, height),
                    max(x-1, 0):min(x+2, width)
                ]
                n_occupied = (neighborhood == "#").sum()
                if char == "L":
                    if n_occupied == 0:
                        # Seat is empty and neighboring seats are empty.
                        new_seats[y, x] = "#"
                elif n_occupied >= 5:
                    # Seat is occupied and 4 or more neighbors are occupied.
                    # Use ">= 5" because the sum contains the seat itself.
                    new_seats[y, x] = "L"
        if numpy.array_equal(seats, new_seats):
            return (new_seats == "#").sum()
        seats = new_seats


def part_2(seats):
    height, width = seats.shape
    directions = ((1, 0), (1, -1), (0, -1), (-1, -1),
                  (-1, 0), (-1, 1), (0, 1), (1, 1))
    while True:
        new_seats = seats.copy()
        for y, row in enumerate(seats):
            for x, char in enumerate(row):
                if char == ".":
                    continue
                n_occupied = 0
                for dx, dy in directions:
                    x_ = x + dx
                    y_ = y + dy
                    while x_ in range(width) and y_ in range(height):
                        neighbor = seats[y_, x_]
                        if neighbor == ".":
                            x_ += dx
                            y_ += dy
                            continue
                        n_occupied += neighbor == "#"
                        break
                if char == "L":
                    if n_occupied == 0:
                        new_seats[y, x] = "#"
                elif n_occupied >= 5:
                    new_seats[y, x] = "L"
        if numpy.array_equal(seats, new_seats):
            return (new_seats == "#").sum()
        seats = new_seats


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
