# https://adventofcode.com/2020/day/8

from src.util.exceptions import ResultExpectedError
from src.util.inputs import Inputs
from src.util.solution import Solution


class HandheldGameConsole:

    def __init__(self, instructions: list[tuple[str, int]]) -> None:
        self.instructions = instructions
        self.accumulator = 0
        self.pointer = 0  # index of the next instruction to be executed
        self.seen_pointers = {self.pointer}
        self.has_halted = False
        self.in_infinite_loop = False
        self.operations = {
            "acc": self.acc,
            "jmp": self.jmp,
            "nop": self.nop
        }

    def acc(self, n: int) -> None:
        self.accumulator += n
        self.pointer += 1

    def jmp(self, n: int) -> None:
        self.pointer += n

    def nop(self, _) -> None:
        self.pointer += 1

    def check_pointer(self) -> None:
        """Check if program has halted or if there is an infinite loop."""
        if self.pointer >= len(self.instructions):
            self.has_halted = True
        elif self.pointer in self.seen_pointers:
            self.in_infinite_loop = True
        else:
            self.seen_pointers.add(self.pointer)

    def step(self) -> None:
        """Execute only one operation."""
        operation, value = self.instructions[self.pointer]
        # noinspection PyArgumentList
        self.operations[operation](value)
        self.check_pointer()

    def run(self) -> None:
        """Run the machine until it halts or an infinite loop is detected."""
        while not self.has_halted and not self.in_infinite_loop:
            self.step()


class Solution2020Day08(Solution):

    def solve(self, inputs: Inputs) -> None:
        instructions = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(instructions))
        self.sample_results_2.append(self.solve_2(instructions))

        instructions = self.prepare(inputs.input)
        self.result_1 = self.solve_1(instructions)
        self.result_2 = self.solve_2(instructions)

    @staticmethod
    def prepare(data: str) -> list[tuple[str, int]]:
        return [(op, int(val)) for op, val in (line.split() for line in data.splitlines())]

    @staticmethod
    def solve_1(instructions: list[tuple[str, int]]) -> int:
        game_console = HandheldGameConsole(instructions)
        game_console.run()
        return game_console.accumulator

    @staticmethod
    def solve_2(instructions: list[tuple[str, int]]) -> int:
        for i, (operation, value) in enumerate(instructions):
            if operation == "jmp":
                modified = ("nop", value)
            elif operation == "nop":
                modified = ("jmp", value)
            else:
                continue
            modified_instructions = instructions.copy()
            modified_instructions[i] = modified
            game_console = HandheldGameConsole(modified_instructions)
            game_console.run()
            if game_console.has_halted:
                return game_console.accumulator
        raise ResultExpectedError
