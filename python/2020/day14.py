# https://adventofcode.com/2020/day/14

import itertools
import re


def get_data(filename):
    with open(filename) as file:
        data = file.read().split("\n\n")
    data = [block.splitlines() for block in data]
    if len(data) == 1:
        return data[0]
    return data


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


sample_data = get_data("../../input/2020-14-sample.txt")
challenge_data = get_data("../../input/2020-14-input.txt")

if __name__ == "__main__":
    assert part_1(sample_data[0]) == 165
    assert part_2(sample_data[1]) == 208

    print(part_1(challenge_data))  # 4297467072083
    print(part_2(challenge_data))  # 5030603328768
