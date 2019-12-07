# https://adventofcode.com/2019/day/2


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
for noun in range(100):
    for verb in range(100):
        program[1] = noun
        program[2] = verb
        computer = IntcodeComputer(program)
        computer.run()
        if computer.intcode[0] == target:
            break
    else:
        continue
    break
print(100 * noun + verb)  # 8478
