# https://adventofcode.com/2019/day/5


from intcode import IntcodeComputer


with open("day_05_input.txt", "r") as file:
    program = [int(i) for i in file.read().split(",")]
computer = IntcodeComputer(program)
# Part 1:
computer.run([1])  # a bunch of zeros and then 9006673
# Part 2:
computer.run([5])  # 3629692
