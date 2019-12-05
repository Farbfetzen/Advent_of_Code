# https://adventofcode.com/2019/day/5


# FIXME: This is not yet working.

def run_intcode(intcode):
    i = 0
    while True:
        instruction = str(intcode[i])
        print(instruction)
        if len(instruction) == 1:
            instruction = "000" + instruction
        elif len(instruction) == 2:
            instruction = "00" + instruction
        elif len(instruction) == 3:
            instruction = "0" + instruction
        *parameters, op10, op1 = (int(i) for i in instruction)
        opcode = 10 * op10 + op1
        # print(opcode)
        # print(parameters)
        if opcode in [1, 2]:
            param_1_mode = parameters[-1]
            if param_1_mode == 0:
                a = intcode[intcode[i + 1]]
            elif param_1_mode == 1:
                a = intcode[i + 1]
            param_2_mode = parameters[-2]
            if param_2_mode == 0:
                b = intcode[intcode[i + 2]]
            elif param_2_mode == 1:
                b = intcode[i + 2]
            if opcode == 1:
                intcode[intcode[i + 3]] = a + b
            else:
                intcode[intcode[i + 3]] = a * b
            i += 3
        elif opcode == 3:
            intcode[intcode[i + 1]] = int(input("enter an integer: "))
            i += 2
        elif opcode == 4:
            param_mode = parameters[-1]
            if param_mode == 0:
                print(intcode[intcode[i + 1]])
            elif param_mode == 1:
                print(intcode[i + 1])
            i += 2
        elif opcode == 99:
            break
        else:
            raise ValueError("unexpected opcode")


with open("day_05_input.txt", "r") as file:
    program = [int(i) for i in file.read().split(",")]
run_intcode(program)
