# https://adventofcode.com/2020/day/11

import numpy

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2020Day11(Solution):

    def solve(self, inputs: Inputs) -> None:
        seats = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(seats))
        self.sample_results_2.append(self.solve_2(seats))

        seats = self.prepare(inputs.input)
        self.result_1 = self.solve_1(seats)
        self.result_2 = self.solve_2(seats)

    @staticmethod
    def prepare(data: str) -> numpy.ndarray:
        return numpy.array([list(line) for line in data.splitlines()])

    @staticmethod
    def solve_1(seats: numpy.ndarray) -> int:
        height, width = seats.shape
        while True:
            new_seats = seats.copy()
            for y, row in enumerate(seats):
                for x, char in enumerate(row):
                    if char == ".":
                        continue
                    neighborhood = seats[
                                   max(y - 1, 0):min(y + 2, height),
                                   max(x - 1, 0):min(x + 2, width)
                                   ]
                    # noinspection PyUnresolvedReferences
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
                # noinspection PyUnresolvedReferences
                return (new_seats == "#").sum()
            seats = new_seats

    @staticmethod
    def solve_2(seats: numpy.ndarray) -> int:
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
                # noinspection PyUnresolvedReferences
                return (new_seats == "#").sum()
            seats = new_seats
