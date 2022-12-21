# https://adventofcode.com/2019/day/2

import itertools

from src.util.types import Data, Solution
from src.year2019.intcode import IntcodeComputer


def prepare_data(data: str) -> IntcodeComputer:
    program = [int(i) for i in data.split(",")]
    program[1] = 12
    program[2] = 2
    return IntcodeComputer(program)


def part_1(computer: IntcodeComputer) -> int:
    computer.run()
    return computer.intcode[0]


def part_2(computer: IntcodeComputer) -> int:
    target = 19690720
    for noun, verb in itertools.product(range(100), repeat=2):
        computer.original_intcode[1] = noun
        computer.original_intcode[2] = verb
        computer.reset()
        computer.run()
        if computer.intcode[0] == target:
            return 100 * noun + verb
    raise RuntimeError("Should have returned a result.")


def solve(data: Data) -> Solution:
    solution = Solution()
    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
