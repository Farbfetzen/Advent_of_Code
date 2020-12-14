# https://adventofcode.com/2019/day/17


import math

from intcode import IntcodeComputer


with open("day_17_input.txt") as file:
    code = [int(i) for i in file.read().split(",")]

droid = IntcodeComputer(code, True, True, ascii_mode=True)
scaffold = droid.run_ascii()
# print(scaffold)
scaffold = scaffold.strip().splitlines()


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


# part 2
droid.reset()
droid.intcode[0] = 2

# Manually constructed path. Not sure how I would do this automatically.
# A     R, 6, L, 8, R, 8,
# A     R, 6, L, 8, R, 8,
# B     R, 4, R, 6, R, 6, R, 4, R, 4,
# C     L, 8, R, 6, L, 10, L, 10,
# B     R, 4, R, 6, R, 6, R, 4, R, 4,
# C     L, 8, R, 6, L, 10, L, 10,
# B     R, 4, R, 6, R, 6, R, 4, R, 4,
# C     L, 8, R, 6, L, 10, L, 10,
# A     R, 6, L, 8, R, 8,
# C     L, 8, R, 6, L, 10, L, 10

main_routine = "A,A,B,C,B,C,B,C,A,C"
A = "R,6,L,8,R,8"
B = "R,4,R,6,R,6,R,4,R,4"
C = "L,8,R,6,L,10,L,10"
video_feed = "n"  # or "y" but I did not implement a display.

output = droid.run_ascii()
# print(output)  # The map and then "Main:"

output = droid.run_ascii(main_routine)
# print(output)  # prints "Function A:"

output = droid.run_ascii(A)
# print(output)  # prints "Function B:"

output = droid.run_ascii(B)
# print(output)  # prints "Function C:"

output = droid.run_ascii(C)
# print(output)  # prints "Continuous video feed?"

output = droid.run_ascii(video_feed)
# print(output)  # prints the final state of the map and the solution number

print(ord(output[-1]))  # 926819
