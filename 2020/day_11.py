# https://adventofcode.com/2020/day/11


# Both parts are too slow for my taste. Maybe I'll improve this sometime.


import numpy


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


test_input = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".splitlines()
test_input = numpy.array([list(line) for line in test_input])
assert part_1(test_input) == 37
assert part_2(test_input) == 26

with open("day_11_input.txt") as file:
    challenge_input = file.read().splitlines()
challenge_input = numpy.array([list(line) for line in challenge_input])
print(part_1(challenge_input))  # 2299
print(part_2(challenge_input))  # 2047
