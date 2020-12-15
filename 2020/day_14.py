# https://adventofcode.com/2020/day/14

import itertools
import re


def part_1(program):
    memory = {}
    mask_to_0 = 0
    mask_to_1 = 0
    for line in program:
        if line[:4] == "mask":
            mask = line[7:]
            mask_to_1 = int("".join(m if m == "1" else "0" for m in mask), 2)
            mask_to_0 = int("".join(m if m == "0" else "1" for m in mask), 2)
        else:
            address, value = (int(x) for x in re.findall(r"(\d+)", line))
            memory[address] = (value | mask_to_1) & mask_to_0
    return sum(memory.values())


def part_2(program):
    memory = {}
    mask_to_1 = 0
    mask_float = ""
    n_floats = 0
    for line in program:
        if line[:4] == "mask":
            mask = line[7:]
            mask_to_1 = int("".join(m if m == "1" else "0" for m in mask), 2)
            n_floats = mask.count("X")
            mask_float = "".join("{}" if m == "X" else "0" for m in mask)
        else:
            address, value = (int(x) for x in re.findall(r"(\d+)", line))
            address = address | mask_to_1
            for bits in itertools.product("01", repeat=n_floats):
                modified_mask = mask_float.format(*bits)
                memory[address ^ int(modified_mask, 2)] = value
    return sum(memory.values())


test_input_1 = """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""".splitlines()
assert part_1(test_input_1) == 165

test_input_2 = """\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".splitlines()
assert part_2(test_input_2) == 208

with open("day_14_input.txt") as file:
    challenge_input = file.read().splitlines()
print(part_1(challenge_input))  # 4297467072083
print(part_2(challenge_input))  # 5030603328768
