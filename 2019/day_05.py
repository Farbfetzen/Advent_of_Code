# https://adventofcode.com/2019/day/5


def run_intcode(intcode):
    position_mode = "0"
    immediate_mode = "1"
    i = 0
    while True:
        instruction = str(intcode[i])
        instruction = instruction.zfill(5)
        param3, param2, param1 = instruction[:3]
        opcode = instruction[3:]
        if opcode in "0102":
            if param1 == position_mode:
                a = intcode[intcode[i + 1]]
            elif param1 == immediate_mode:
                a = intcode[i + 1]
            if param2 == position_mode:
                b = intcode[intcode[i + 2]]
            elif param2 == immediate_mode:
                b = intcode[i + 2]
            if opcode == "01":
                intcode[intcode[i + 3]] = a + b
            else:
                intcode[intcode[i + 3]] = a * b
            i += 4
        elif opcode == "03":
            intcode[intcode[i + 1]] = int(input("enter an integer: "))
            i += 2
        elif opcode == "04":
            if param1 == position_mode:
                print(intcode[intcode[i + 1]])
            elif param1 == immediate_mode:
                print(intcode[i + 1])
            i += 2
        elif opcode == "99":
            break
        else:
            raise ValueError(f"unexpected opcode: {opcode}")


with open("day_05_input.txt", "r") as file:
    program = [int(i) for i in file.read().split(",")]
run_intcode(program)


# Solution of part 1: 9006673
