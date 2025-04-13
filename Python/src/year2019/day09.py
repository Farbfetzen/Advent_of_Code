# https://adventofcode.com/2019/day/9


from intcode_deprecated import IntcodeComputerDeprecated


with open("../../input/2019-09-input.txt") as file:
    program = [int(i) for i in file.read().split(",")]
computer = IntcodeComputerDeprecated(program)
computer.run([1])  # 2457252183
computer.reset()
computer.run([2])  # 70634
