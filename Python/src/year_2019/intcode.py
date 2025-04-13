from collections import defaultdict
from collections.abc import Sequence


class IntcodeComputer:

    def __init__(self, program: list[int], inputs: Sequence[int] = None) -> None:
        self.memory = defaultdict(int, {k: v for k, v in enumerate(program)})
        self.inputs = inputs

        self.opcode = "99"
        self.opcode_methods = {
            "01": self.add,
            "02": self.multiply,
            "03": self.read_input,
            "04": self.store_output,
            "05": self.jump_if_true,
            "06": self.jump_if_false,
            "07": self.less_than,
            "08": self.equals,
            "99": self.halt
        }
        self.parameter_modes = ("0", "0", "0")
        self.instruction_pointer = 0
        self.input_pointer = 0
        self.halted = False
        self.output: list[int] = []

    def run(self) -> None:
        while not self.halted:
            self.read_instruction()
            self.opcode_methods[self.opcode]()

    def add(self) -> None:
        first_position, second_position, target_position = self.get_positions(3)
        self.memory[target_position] = self.memory[first_position] + self.memory[second_position]

    def multiply(self) -> None:
        first_position, second_position, target_position = self.get_positions(3)
        self.memory[target_position] = self.memory[first_position] * self.memory[second_position]

    def read_input(self) -> None:
        target_position = self.get_positions(1)[0]
        self.memory[target_position] = self.inputs[self.input_pointer]
        self.input_pointer += 1

    def store_output(self) -> None:
        value_position = self.get_positions(1)[0]
        self.output.append(self.memory[value_position])

    def jump_if_true(self) -> None:
        test_position, target_position = self.get_positions(2)
        if self.memory[test_position] != 0:
            self.instruction_pointer = self.memory[target_position]

    def jump_if_false(self) -> None:
        test_position, target_position = self.get_positions(2)
        if self.memory[test_position] == 0:
            self.instruction_pointer = self.memory[target_position]

    def less_than(self) -> None:
        first_position, second_position, target_position = self.get_positions(3)
        self.memory[target_position] = int(self.memory[first_position] < self.memory[second_position])

    def equals(self) -> None:
        first_position, second_position, target_position = self.get_positions(3)
        self.memory[target_position] = int(self.memory[first_position] == self.memory[second_position])

    def halt(self) -> None:
        self.halted = True

    def read_instruction(self) -> None:
        """Split an instruction into opcode and parameter modes.
        The instruction is read from right to left.
        The first two digits are the opcode.
        The other three are the parameter modes.
        Missing digits are assumed to be 0.
        Example: 2102 represents the opcode 02 and parameter modes 1, 2, and 0.
        """
        instruction = str(self.memory[self.instruction_pointer]).zfill(5)
        self.opcode = instruction[-2:]
        self.parameter_modes = tuple(instruction[-3::-1])

    def get_positions(self, n: int) -> list[int]:
        """Determine the positions of the values according to the parameters and parameter modes.

        :param n: Number of parameters to parse.
        :return: The positions of the values.
        """
        positions = []
        self.instruction_pointer += 1
        for i in range(n):
            if self.parameter_modes[i] == "0":
                # position mode
                positions.append(self.memory[self.instruction_pointer + i])
            elif self.parameter_modes[i] == "1":
                # immediate mode
                positions.append(self.instruction_pointer + i)
        self.instruction_pointer += n
        return positions
