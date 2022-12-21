from collections import defaultdict


class IntcodeComputer:
    def __init__(self, intcode, silent=False,
                 feedback_mode=False, ascii_mode=False):
        self.intcode = defaultdict(int, {i: x for i, x in enumerate(intcode)})
        self.original_intcode = self.intcode.copy()
        self.silent = silent
        self.feedback_mode = feedback_mode
        self.ascii_mode = ascii_mode
        self.inputs = None
        self.pointer = 0
        self.relative_base = 0
        self.has_halted = False
        self.is_paused = False
        self.output = None
        self.get_position = (
            self.get_position_in_position_mode,
            self.get_position_in_immediate_mode,
            self.get_position_in_relative_mode
        )
        self.opcode_methods = {
            1: self.add,
            2: self.multiply,
            3: self.read,
            4: self.print_and_or_pause,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            9: self.change_relative_base,
            99: self.halt
        }

    def reset(self):
        self.intcode = self.original_intcode.copy()
        self.pointer = 0
        self.relative_base = 0
        self.has_halted = False
        self.is_paused = False
        self.output = None

    def get_next_instruction(self):
        instruction = str(self.intcode[self.pointer])
        opcode = int(instruction[-2:])
        parameters = [int(i) for i in instruction[-3::-1]]
        return opcode, parameters

    def run(self, inputs=None):
        if inputs is not None:
            if self.ascii_mode:
                inputs = [ord(inp) for inp in inputs]
                ascii_newline = ord("\n")
                if inputs[-1] != ascii_newline:
                    inputs.append(ascii_newline)
            # Reverse input because popping from the end is better.
            self.inputs = list(reversed(inputs))
        self.output = None
        self.is_paused = False
        while not (self.has_halted or self.is_paused):
            opcode, parameters = self.get_next_instruction()
            self.opcode_methods[opcode](parameters)
        if self.ascii_mode and self.output is not None:
            if self.output <= 0x10ffff:  # max value for chr()
                self.output = chr(self.output)
            else:
                self.output = str(self.output)
        return self.output

    def run_ascii(self, instructions=None):
        # Catch all the output into one string.
        # This is a bit hacky with the try...except... but I can't be bothered
        # to figure out where the errors come from.
        # This will also remain a method separate from self.run().
        output = [self.run(instructions)]
        while not self.has_halted:
            try:
                output.append(self.run())
            except (AttributeError, IndexError):
                break
        return "".join(x for x in output if x is not None)

    def get_positions(self, parameters, n):
        parameters += [0] * (n - len(parameters))
        return [self.get_position[param](pos)
                for pos, param in enumerate(parameters)]

    def get_position_in_position_mode(self, position):
        return self.intcode[self.pointer + position + 1]

    def get_position_in_immediate_mode(self, position):
        return self.pointer + position + 1

    def get_position_in_relative_mode(self, position):
        return self.intcode[self.pointer + position + 1] + self.relative_base

    def add(self, parameters):
        a, b, target = self.get_positions(parameters, 3)
        self.intcode[target] = self.intcode[a] + self.intcode[b]
        self.pointer += 4

    def multiply(self, parameters):
        a, b, target = self.get_positions(parameters, 3)
        self.intcode[target] = self.intcode[a] * self.intcode[b]
        self.pointer += 4

    def read(self, parameters):
        position = self.get_positions(parameters, 1)[0]
        self.intcode[position] = self.inputs.pop()
        self.pointer += 2

    def print_and_or_pause(self, parameters):
        position = self.get_positions(parameters, 1)[0]
        self.output = self.intcode[position]
        if not self.silent:
            print(self.output)
        if self.feedback_mode:
            self.is_paused = True
        self.pointer += 2

    def jump_if_true(self, parameters):
        position, target = self.get_positions(parameters, 2)
        if self.intcode[position]:
            self.pointer = self.intcode[target]
        else:
            self.pointer += 3

    def jump_if_false(self, parameters):
        position, target = self.get_positions(parameters, 2)
        if self.intcode[position] == 0:
            self.pointer = self.intcode[target]
        else:
            self.pointer += 3

    def less_than(self, parameters):
        a, b, target = self.get_positions(parameters, 3)
        self.intcode[target] = int(self.intcode[a] < self.intcode[b])
        self.pointer += 4

    def equals(self, parameters):
        a, b, target = self.get_positions(parameters, 3)
        self.intcode[target] = int(self.intcode[a] == self.intcode[b])
        self.pointer += 4

    def change_relative_base(self, parameters):
        position = self.get_positions(parameters, 1)[0]
        self.relative_base += self.intcode[position]
        self.pointer += 2

    def halt(self, parameters):
        self.has_halted = True
