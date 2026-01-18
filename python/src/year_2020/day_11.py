# https://adventofcode.com/2020/day/11

from typing import Callable

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

    def solve_1(self, seats: numpy.ndarray) -> int:
        return self.iterate_seats(seats, self.count_neighbors_1)

    def solve_2(self, seats: numpy.ndarray) -> int:
        return self.iterate_seats(seats, self.count_neighbors_2)

    def iterate_seats(self, seats: numpy.ndarray, neighbor_counter: Callable[[numpy.ndarray, int, int], int]) -> int:
        while True:
            new_seats = seats.copy()
            for (y, x), seat in numpy.ndenumerate(seats):
                if seat != ".":
                    n_occupied = neighbor_counter(seats, x, y)
                    self.update_seat(new_seats, seat, n_occupied, x, y)
            if numpy.array_equal(seats, new_seats):
                return int((new_seats == "#").sum())
            seats = new_seats

    @staticmethod
    def count_neighbors_1(seats: numpy.ndarray, x: int, y: int) -> int:
        height, width = seats.shape
        neighborhood = seats[max(y - 1, 0) : min(y + 2, height), max(x - 1, 0) : min(x + 2, width)]
        return int((neighborhood == "#").sum())

    @staticmethod
    def count_neighbors_2(seats: numpy.ndarray, x: int, y: int) -> int:
        height, width = seats.shape
        directions = ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1))
        n_occupied = 0
        for dx, dy in directions:
            neighbor_x = x + dx
            neighbor_y = y + dy
            while 0 <= neighbor_x < width and 0 <= neighbor_y < height:
                neighbor = seats[neighbor_y, neighbor_x]
                if neighbor != ".":
                    n_occupied += neighbor == "#"
                    break
                neighbor_x += dx
                neighbor_y += dy
        return n_occupied

    @staticmethod
    def update_seat(new_seats: numpy.ndarray, seat: str, n_occupied: int, x: int, y: int) -> None:
        if seat == "L" and n_occupied == 0:
            # Seat is empty and neighboring seats are empty.
            new_seats[y, x] = "#"
        elif n_occupied >= 5:
            # Seat is occupied and 5 or more neighbors are occupied.
            # Use ">= 5" for part 1 because the sum contains the seat itself.
            new_seats[y, x] = "L"
