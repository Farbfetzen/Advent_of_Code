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
    i = 0
    while True:
        i += 1
        new_seats = seats.copy()
        for y, row in enumerate(seats):
            for x, char in enumerate(row):
                if char == ".":
                    continue
                topleft = seats[y::-1, x::-1]
                top = topleft[1:, 0]
                left = topleft[0, 1:]
                topleft = numpy.diagonal(topleft)[1:]
                bottomright = seats[y:, x:]
                bottom = bottomright[1:, 0]
                right = bottomright[0, 1:]
                bottomright = numpy.diagonal(bottomright)[1:]
                topright = numpy.diagonal(seats[y::-1, x:])[1:]
                bottomleft = numpy.diagonal(seats[y:, x::-1])[1:]
                n_occupied = 0
                for view_direction in (left, right, top, bottom,
                                       topleft, topright,
                                       bottomleft, bottomright):

                    nonempty = view_direction[view_direction != "."]
                    if nonempty.size > 0 and nonempty[0] == "#":
                        n_occupied += 1
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
