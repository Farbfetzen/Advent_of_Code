# https://adventofcode.com/2019/day/17


import math

from intcode import IntcodeComputer


with open("day_17_input.txt", "r") as file:
    code = [int(i) for i in file.read().split(",")]

scaffold_mapper = IntcodeComputer(code, True, True)
chars = ""
while not scaffold_mapper.has_halted:
    char = scaffold_mapper.run()
    if char is not None:
        chars += chr(int(char))
# print(chars)
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


# part 2
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


def to_ascii(instructions):
    return [ord(instr) for instr in instructions]


main_routine = to_ascii("A,A,B,C,B,C,B,C,A,C\n")
A = to_ascii("R,6,L,8,R,8\n")
B = to_ascii("R,4,R,6,R,6,R,4,R,4\n")
C = to_ascii("L,8,R,6,L,10,L,10\n")
video_feed = to_ascii("n\n")  # or "y\n" but I did not implement a display.

# print(main_routine)
# print(A)
# print(B)
# print(C)
# print(video_feed)

code[0] = 2
robot = IntcodeComputer(code, True, True)


def run_robot(instructions=None):
    # This is kind of messy. I don't know why some exceptions occur so I just
    # use try...except and break on exception. Debugging the
    # intcode computer is annoying and this works anyway so who cares.
    output = []
    if instructions is not None:
        output.append(robot.run(instructions))
    while not robot.has_halted:
        try:
            output.append(robot.run())
        except (AttributeError, IndexError):
            break
    return "".join(chr(x) for x in output if x is not None)


output = run_robot()
# print(output)  # The map and then "Main:"

output = run_robot(main_routine)
# print(output)  # prints "Function A:"

output = run_robot(A)
# print(output)  # prints "Function B:"

output = run_robot(B)
# print(output)  # prints "Function C:"

output = run_robot(C)
# print(output)  # prints "Continuous video feed?"

output = run_robot(video_feed)
# print(output)  # prints the final state of the map and "󢑣"

print(ord(output[-1]))  # 926819


# my scaffold:
# ............###########..........................
# ............#.........#..........................
# ............#.........#..........................
# ............#.........#..........................
# ............#.........#..........................
# ............#.........#..........................
# ............#.........#########..................
# ............#.................#..................
# ......#########...............#..................
# ......#.....#.#...............#..................
# ......#.....#.#...............#..................
# ......#.......#...............#..................
# ......#.......#...............#..................
# ......#.......#...............#..................
# ......#.......#########.......#########..........
# ......#...............#...............#..........
# ^######...........#######.............#..........
# ..................#...#.#.............#..........
# ..................#...#.#.............#..........
# ..................#...#.#.............#..........
# ..................#.#####.............###########
# ..................#.#.#.........................#
# ..................#####.........................#
# ....................#...........................#
# ....................#...........................#
# ....................#...........................#
# ....................#...........................#
# ....................#...........................#
# ..............#######...........................#
# ..............#.................................#
# ..............#...........................#######
# ..............#...........................#......
# ..............#...........................#......
# ..............#...........................#......
# ..............#...........................#......
# ..............#...........................#......
# ..............#...#####.................#####....
# ..............#...#...#.................#.#.#....
# ..............###########.............#####.#....
# ..................#...#.#.............#.#...#....
# ..................#...#########.......#.#...#....
# ..................#.....#.....#.......#.#...#....
# ..................#######.....#.......#######....
# ..............................#.........#........
# ..............................#.........#........
# ..............................#.........#........
# ..............................###########........
