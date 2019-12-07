# https://adventofcode.com/2019/day/5


from intcode import IntcodeComputer


with open("day_05_input.txt", "r") as file:
    program = [int(i) for i in file.read().split(",")]
computer = IntcodeComputer(program)
computer.run()


# Part 1: input = 1, output = a bunch of zeros and then 9006673
# Part 2: input = 5, output = 3629692
