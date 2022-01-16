# https://adventofcode.com/2019/day/2


import itertools

from intcode import IntcodeComputer


INPUT_PATH = "../../input/2019-02-input.txt"


def get_data(filename):
    with open(filename) as file:
        program = [int(i) for i in file.read().split(",")]
    program[1] = 12
    program[2] = 2
    return IntcodeComputer(program)


def part_1(computer):
    computer.run()
    return computer.intcode[0]


def part_2(computer):
    target = 19690720
    for noun, verb in itertools.product(range(100), repeat=2):
        computer.original_intcode[1] = noun
        computer.original_intcode[2] = verb
        computer.reset()
        computer.run()
        if computer.intcode[0] == target:
            return 100 * noun + verb


if __name__ == "__main__":
    challenge_data = get_data(INPUT_PATH)
    print(part_1(challenge_data))  # 3101844
    print(part_2(challenge_data))  # 8478
