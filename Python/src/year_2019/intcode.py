from collections import defaultdict
from typing import Callable


class IntcodeComputer:

    def __init__(self, program: list[int]) -> None:
        self.memory = defaultdict(int, {k: v for k, v in enumerate(program)})
        self.opcode_methods: dict[str, Callable[[], None]] = {
            "1": self.add,
            "2": self.multiply,
            "99": self.halt
        }
        self.instruction_pointer = 0
        self.halted = False

    def run(self) -> None:
        while not self.halted:
            opcode = str(self.memory[self.instruction_pointer])
            self.opcode_methods[opcode]()
        # FIXME: ACHTUNG: Parameter sind die auf den Opcode folgenden Werte!
        #  Nicht die restlichen Ziffern in der Instruction! Die sind "parameter modes".
        #  Das habe ich im alten Computer falsch benannt, was beim Lesen der Problembeschreibung verwirrt.

    def add(self) -> None:
        position_a = self.memory[self.instruction_pointer + 1]
        position_b = self.memory[self.instruction_pointer + 2]
        target_position = self.memory[self.instruction_pointer + 3]
        self.memory[target_position] = self.memory[position_a] + self.memory[position_b]
        self.instruction_pointer += 4

    def multiply(self) -> None:
        position_a = self.memory[self.instruction_pointer + 1]
        position_b = self.memory[self.instruction_pointer + 2]
        target_position = self.memory[self.instruction_pointer + 3]
        self.memory[target_position] = self.memory[position_a] * self.memory[position_b]
        self.instruction_pointer += 4

    def halt(self) -> None:
        self.halted = True
