# https://adventofcode.com/2020/day/11

# TODO: Improve the performance of both parts.


import numpy


SAMPLE_PATH = "../../input/2020-11-sample.txt"
INPUT_PATH = "../../input/2020-11-input.txt"


def get_data(filename):
    with open(filename) as file:
        data = file.read().splitlines()
    return numpy.array([list(line) for line in data])


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


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(sample_data) == 37
    assert part_2(sample_data) == 26

    challenge_data = get_data(INPUT_PATH)
    print(part_1(challenge_data))  # 2299
    print(part_2(challenge_data))  # 2047
