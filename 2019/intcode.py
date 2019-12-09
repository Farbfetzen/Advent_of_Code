from defaultlist import defaultlist


class IntcodeComputer:
    def __init__(self, intcode, silent=False, feedback_mode=False):
        self.original_intcode = defaultlist(lambda: 0) + intcode
        self.intcode = self.original_intcode.copy()
        self.silent = silent
        self.feedback_mode = feedback_mode
        self.inputs = None
        self.pointer = 0
        self.relative_base = 0
        self.params = ""
        self.opcodes = {
            1: self.add,
            2: self.mult,
            3: self.read,
            4: self.print,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            9: self.adjust_relative_base
        }
        self.out_value = None
        self.has_halted = False

    def run(self, inputs=None, reset=True):
        if reset:
            self.intcode = self.original_intcode.copy()
            self.pointer = 0
            self.relative_base = 0
            self.out_value = None
            self.has_halted = False
        if inputs is not None:
            # reverse input because popping from the right end is better
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

    def get_indices(self, n):
        self.params = self.params.ljust(n, "0")
        indices = []
        for i, p in enumerate(self.params):
            if p == "0":  # position_mode
                position = self.intcode[self.pointer + i + 1]
            elif p == "1":  # immediate_mode
                position = self.pointer + i + 1
            elif p == "2":  # relative_mode
                position = self.intcode[self.pointer + i + 1] + self.relative_base
            else:
                raise ValueError(f"unknown parameter mode: {p}")
            indices.append(position)
        return indices

    def add(self):
        a, b, target = self.get_indices(3)
        self.intcode[target] = self.intcode[a] + self.intcode[b]
        self.pointer += 4

    def mult(self):
        a, b, target = self.get_indices(3)
        self.intcode[target] = self.intcode[a] * self.intcode[b]
        self.pointer += 4

    def read(self):
        self.intcode[self.get_indices(1)[0]] = self.inputs.pop()
        self.pointer += 2

    def print(self):
        self.out_value = self.intcode[self.get_indices(1)[0]]
        if not self.silent:
            print(self.out_value)
        self.pointer += 2

    def jump_if_true(self):
        i, target = self.get_indices(2)
        if self.intcode[i] != 0:
            self.pointer = self.intcode[target]
        else:
            self.pointer += 3

    def jump_if_false(self):
        i, target = self.get_indices(2)
        if self.intcode[i] == 0:
            self.pointer = self.intcode[target]
        else:
            self.pointer += 3

    def less_than(self):
        a, b, target = self.get_indices(3)
        self.intcode[target] = int(self.intcode[a] < self.intcode[b])
        self.pointer += 4

    def equals(self):
        a, b, target = self.get_indices(3)
        self.intcode[target] = int(self.intcode[a] == self.intcode[b])
        self.pointer += 4

    def adjust_relative_base(self):
        self.relative_base += self.intcode[self.get_indices(1)[0]]
        self.pointer += 2
