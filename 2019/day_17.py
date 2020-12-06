# https://adventofcode.com/2019/day/17


import math

from intcode import IntcodeComputer


with open("day_17_input.txt", "r") as file:
    code = [int(i) for i in file.read().split(",")]

robot = IntcodeComputer(code, True, True)
chars = ""
while not robot.has_halted:
    char = robot.run()
    if char is not None:
        chars += chr(int(char))
scaffold = chars.strip().splitlines()


# part 1
intersections = []
width = len(scaffold[0])
height = len(scaffold)
for x in range(1, width - 1):
    for y in range(1, height - 1):
        if (scaffold[y][x] == "#"
                and scaffold[y - 1][x] == "#"
                and scaffold[y + 1][x] == "#"
                and scaffold[y][x - 1] == "#"
                and scaffold[y][x + 1] == "#"):
            intersections.append((x, y))
alignments = [math.prod(x) for x in intersections]
print(sum(alignments))  # 8520



