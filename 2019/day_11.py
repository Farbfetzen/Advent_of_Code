# https://adventofcode.com/2019/day/11


import collections
import numpy as np

from intcode import IntcodeComputer


def paint(starting_color):
    robot.reset()
    panels = collections.defaultdict(int)
    x, y = 0, 0
    panels[(x, y)] = starting_color  # 0 = black, 1 = white
    # right, down, left, up
    dx = (1, 0, -1, 0)
    dy = (0, -1, 0, 1)
    d_i = 3
    left_or_right = (-1, 1)
    while not robot.has_halted:
        panels[(x, y)] = robot.run([panels[(x, y)]])
        if robot.has_halted:
            break
        d_i = (d_i + left_or_right[robot.run()]) % 4
        x += dx[d_i]
        y += dy[d_i]
    return panels


with open("day_11_input.txt") as file:
    program = [int(i) for i in file.read().split(",")]
robot = IntcodeComputer(program, True, True)

# part 1:
print(len(paint(0)))  # 2428

# part 2:
image = paint(1)
x_min = min(image.keys())[0]
x_max = max(image.keys())[0]
y_min = min(image.keys(), key=lambda v: v[1])[1]
y_max = max(image.keys(), key=lambda v: v[1])[1]
registration = np.full((y_max - y_min + 1, x_max - x_min + 1), " ")
for k, v in image.items():
    x, y = k
    x -= x_min
    y -= y_min
    if v == 0:
        registration[y, x] = " "
    elif v == 1:
        registration[y, x] = "█"
registration = np.flip(registration, 0)
registration = np.apply_along_axis(
    lambda line: "".join(line),
    1,
    registration
)
registration = "\n".join(registration)
print(registration)  # RJLFBUCU
