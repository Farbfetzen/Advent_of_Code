class IntcodeComputer:
    position_mode = "0"
    immediate_mode = "1"

    def __init__(self, intcode, silent=True, feedback_mode=False):
        self.original_intcode = intcode.copy()
        self.intcode = self.original_intcode.copy()
        self.silent = silent
        self.feedback_mode = feedback_mode
        self.inputs = None
        self.pointer = 0
        self.params = ""
        self.opcodes = {
            1: self.add,
            2: self.mult,
            3: self.read,
            4: self.print,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals
        }
        self.out_value = None
        self.has_halted = False

    def run(self, inputs=None, reset=True):
        if reset:
            self.intcode = self.original_intcode.copy()
            self.pointer = 0
            self.out_value = None
            self.has_halted = False
        if inputs is not None:
            self.inputs = list(reversed(inputs))
        while True:
            instruction = str(self.intcode[self.pointer])
            opcode = int(instruction[-2:])
            self.params = instruction[-3::-1]
            if opcode == 99:
                self.has_halted = True
                break
            else:
                self.opcodes[opcode]()
                if self.feedback_mode and opcode == 4:
                    break
        return self.out_value

    def get_values(self, n):
        self.params = self.params.ljust(n, "0")
        values = []
        for i, p in enumerate(self.params):
            if p == self.position_mode:
                position = self.intcode[self.pointer + i + 1]
            elif p == self.immediate_mode:
                position = self.pointer + i + 1
            else:
                raise ValueError(f"unknown parameter mode: {p}")
            values.append(self.intcode[position])
        return values

    def add(self):
        target_position = self.intcode[self.pointer + 3]
        values = self.get_values(2)
        self.intcode[target_position] = sum(values)
        self.pointer += 4

    def mult(self):
        target_position = self.intcode[self.pointer + 3]
        values = self.get_values(2)
        self.intcode[target_position] = values[0] * values[1]
        self.pointer += 4

    def read(self):
        target_position = self.intcode[self.pointer + 1]
        self.intcode[target_position] = self.inputs.pop()
        self.pointer += 2

    def print(self):
        self.out_value = self.get_values(1)[0]
        if not self.silent:
            print(self.out_value)
        self.pointer += 2

    def jump_if_true(self):
        values = self.get_values(2)
        if values[0] != 0:
            self.pointer = values[1]
        else:
            self.pointer += 3

    def jump_if_false(self):
        values = self.get_values(2)
        if values[0] == 0:
            self.pointer = values[1]
        else:
            self.pointer += 3

    def less_than(self):
        values = self.get_values(2)
        output = int(values[0] < values[1])
        target_position = self.intcode[self.pointer + 3]
        self.intcode[target_position] = output
        self.pointer += 4

    def equals(self):
        values = self.get_values(2)
        output = int(values[0] == values[1])
        target_position = self.intcode[self.pointer + 3]
        self.intcode[target_position] = output
        self.pointer += 4
