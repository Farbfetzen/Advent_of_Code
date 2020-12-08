# https://adventofcode.com/2020/day/8


class HandheldGameConsole:
    def __init__(self, instructions):
        if isinstance(instructions, str):
            instructions = self.parse_input(instructions)
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

    @staticmethod
    def parse_input(instruction_str):
        instructions = []
        for instruction in instruction_str.splitlines():
            operation, value = instruction.split()
            instructions.append((operation, int(value)))
        return instructions

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


def part_1(instructions):
    game_console = HandheldGameConsole(instructions)
    game_console.run()
    return game_console.accumulator


def part_2(instructions):
    instructions = HandheldGameConsole.parse_input(instructions)
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


test_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""
assert part_1(test_input) == 5
assert part_2(test_input) == 8

with open("day_08_input.txt") as file:
    challenge_input = file.read()
print(part_1(challenge_input))  # 1262
print(part_2(challenge_input))  # 1643
