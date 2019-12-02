# https://adventofcode.com/2019/day/2


def run_intcode(intcode):
    intcode = intcode.copy()
    i = 0
    opcode = intcode[i]
    while opcode != 99:
        pos_a = intcode[i+1]
        pos_b = intcode[i+2]
        target_pos = intcode[i+3]
        if intcode[i] == 1:
            intcode[target_pos] = intcode[pos_a] + intcode[pos_b]
        elif intcode[i] == 2:
            intcode[target_pos] = intcode[pos_a] * intcode[pos_b]
        else:
            raise ValueError("unexpected integer")
        i += 4
        opcode = intcode[i]
    return intcode[0]


with open("day_02_input.txt", "r") as file:
    program = [int(i) for i in file.read().split(",")]


# part 1
program[1] = 12
program[2] = 2
print(run_intcode(program))


# part 2
target = 19690720
for noun in range(100):
    for verb in range(100):
        program[1] = noun
        program[2] = verb
        if run_intcode(program) == target:
            break
    else:
        continue
    break
print(100 * noun + verb)
