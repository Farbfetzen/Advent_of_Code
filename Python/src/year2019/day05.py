# https://adventofcode.com/2019/day/5


from intcode_deprecated import IntcodeComputerDeprecated


with open("../../input/2019-05-input.txt") as file:
    program = [int(i) for i in file.read().split(",")]
computer = IntcodeComputerDeprecated(program)
# Part 1:
computer.run([1])  # a bunch of zeros and then 9006673
# Part 2:
computer.reset()
computer.run([5])  # 3629692
