from collections import defaultdict


class IntcodeComputer:

    def __init__(self, program: str | list[int]) -> None:
        ints = program if isinstance(program, list) else [int(i) for i in program.split(",")]
        self.memory = defaultdict(int, dict(enumerate(ints)))
        self.inputs: list[int] = []
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
            "09": self.adjust_relative_base,
            "99": self.halt,
        }
        self.parameter_modes = ("0", "0", "0")
        self.instruction_pointer = 0
        self.halted = False
        self.waiting_for_input = False
        self.output: list[int] = []
        self.relative_base = 0

    def run(self, *inputs: int) -> list[int]:
        if inputs:
            # Reverse input because popping from the end is better.
            self.inputs = list(reversed(inputs))
        self.waiting_for_input = False
        self.output.clear()
        while not (self.halted or self.waiting_for_input):
            self.read_instruction()
            self.opcode_methods[self.opcode]()
        return self.output

    def run_ascii(self, inputs: str | None = None) -> list[str | int]:
        if inputs is None:
            int_output = self.run()
        else:
            if inputs[-1] != "\n":
                inputs += "\n"
            int_inputs = (ord(s) for s in inputs)
            int_output = self.run(*int_inputs)
        output: list[str | int] = []
        # Join consecutive strings but keep numbers outside the ascii range 0-255.
        word = []
        for x in int_output:
            if 0 <= x <= 255:
                word.append(chr(x))
            else:
                output.append("".join(word))
                word.clear()
                output.append(x)
        if word:
            output.append("".join(word))
        return output

    def add(self) -> None:
        first_position, second_position, target_position = self.get_positions(3)
        self.memory[target_position] = self.memory[first_position] + self.memory[second_position]

    def multiply(self) -> None:
        first_position, second_position, target_position = self.get_positions(3)
        self.memory[target_position] = self.memory[first_position] * self.memory[second_position]

    def read_input(self) -> None:
        if self.inputs:
            target_position = self.get_positions(1)[0]
            self.memory[target_position] = self.inputs.pop()
        else:
            self.waiting_for_input = True

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

    def adjust_relative_base(self) -> None:
        position = self.get_positions(1)[0]
        self.relative_base += self.memory[position]

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
        self.parameter_modes = (instruction[-3], instruction[-4], instruction[-5])

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
            elif self.parameter_modes[i] == "2":
                # relative mode
                positions.append(self.memory[self.instruction_pointer + i] + self.relative_base)
            else:
                raise ValueError(f"Invalid parameter mode {self.parameter_modes[i]}.")
        self.instruction_pointer += n
        return positions
