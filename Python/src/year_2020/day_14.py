# https://adventofcode.com/2020/day/14

import itertools
import re

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2020Day14(Solution):

    def solve(self, inputs: Inputs) -> None:
        self.sample_results_1.append(self.solve_1(inputs.samples[0].splitlines()))
        self.sample_results_2.append(self.solve_2(inputs.samples[1].splitlines()))

        program = inputs.input.splitlines()
        self.result_1 = self.solve_1(program)
        self.result_2 = self.solve_2(program)

    @staticmethod
    def solve_1(program: list[str]) -> int:
        memory = {}
        mask_to_0 = 0
        mask_to_1 = 0
        for line in program:
            if line.startswith("mask"):
                mask = line[7:]
                mask_to_1 = int("".join(m if m == "1" else "0" for m in mask), 2)
                mask_to_0 = int("".join(m if m == "0" else "1" for m in mask), 2)
            else:
                address, value = (int(x) for x in re.findall(r"(\d+)", line))
                memory[address] = (value | mask_to_1) & mask_to_0
        return sum(memory.values())

    @staticmethod
    def solve_2(program: list[str]) -> int:
        memory = {}
        mask_to_1 = 0
        mask_float = ""
        n_floats = 0
        for line in program:
            if line.startswith("mask"):
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
