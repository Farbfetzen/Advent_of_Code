# https://adventofcode.com/2020/day/8

from src.util.types import Data, Solution


class HandheldGameConsole:
    def __init__(self, instructions):
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

    def acc(self, n):
        self.accumulator += n
        self.pointer += 1

    def jmp(self, n):
        self.pointer += n

    def nop(self, n):
        self.pointer += 1

    def check_pointer(self):
        """Check if program has halted or if there is an infinite loop."""
        if self.pointer >= len(self.instructions):
            self.has_halted = True
        elif self.pointer in self.seen_pointers:
            self.in_infinite_loop = True
        else:
            self.seen_pointers.add(self.pointer)

    def step(self):
        """Execute only one operation."""
        operation, value = self.instructions[self.pointer]
        self.operations[operation](value)
        self.check_pointer()

    def run(self):
        """Run the machine until it halts or an infinite loop is detected."""
        while not self.has_halted and not self.in_infinite_loop:
            self.step()


def prepare_data(data: str) -> list[tuple[str, int]]:
    return [(op, int(val)) for op, val in (line.split() for line in data.splitlines())]


def part_1(instructions):
    game_console = HandheldGameConsole(instructions)
    game_console.run()
    return game_console.accumulator


def part_2(instructions):
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


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
