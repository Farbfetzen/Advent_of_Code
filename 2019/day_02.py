# https://adventofcode.com/2019/day/2


import itertools

from intcode import IntcodeComputer


with open("day_02_input.txt", "r") as file:
    program = [int(i) for i in file.read().split(",")]


# part 1
program[1] = 12
program[2] = 2
computer = IntcodeComputer(program)
computer.run()
print(computer.intcode[0])  # 3101844


# part 2
target = 19690720
for noun, verb in itertools.product(range(100), repeat=2):
    computer.original_intcode[1] = noun
    computer.original_intcode[2] = verb
    computer.reset()
    computer.run()
    if computer.intcode[0] == target:
        break
print(100 * noun + verb)  # 8478
