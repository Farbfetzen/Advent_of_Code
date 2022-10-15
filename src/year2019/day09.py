# https://adventofcode.com/2019/day/9


from intcode import IntcodeComputer


with open("../../input/2019-09-input.txt") as file:
    program = [int(i) for i in file.read().split(",")]
computer = IntcodeComputer(program)
computer.run([1])  # 2457252183
computer.reset()
computer.run([2])  # 70634
