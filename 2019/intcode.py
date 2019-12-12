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
        self.params = []
        self.out_value = None
        self.has_halted = False

    def reset(self):
        self.intcode = self.original_intcode.copy()
        self.pointer = 0
        self.relative_base = 0
        self.out_value = None
        self.has_halted = False

    def run(self, inputs=None):
        if inputs is not None:
            # reverse input because popping from the right end is better
            self.inputs = list(reversed(inputs))
        while True:
            instruction = str(self.intcode[self.pointer])
            opcode = int(instruction[-2:])
            self.params = [int(i) for i in instruction[-3::-1]]
            if opcode == 99:
                self.has_halted = True
                break
            elif opcode == 1:  # add
                a, b, target = self.get_indices(3)
                self.intcode[target] = self.intcode[a] + self.intcode[b]
                self.pointer += 4
            elif opcode == 2:  # mult
                a, b, target = self.get_indices(3)
                self.intcode[target] = self.intcode[a] * self.intcode[b]
                self.pointer += 4
            elif opcode == 3:  # read
                self.intcode[self.get_indices(1)[0]] = self.inputs.pop()
                self.pointer += 2
            elif opcode == 4:  # print or return
                self.out_value = self.intcode[self.get_indices(1)[0]]
                if not self.silent:
                    print(self.out_value)
                self.pointer += 2
                if self.feedback_mode:
                    break
            elif opcode == 5:  # jump if True
                i, target = self.get_indices(2)
                if self.intcode[i] != 0:
                    self.pointer = self.intcode[target]
                else:
                    self.pointer += 3
            elif opcode == 6:  # jump if False
                i, target = self.get_indices(2)
                if self.intcode[i] == 0:
                    self.pointer = self.intcode[target]
                else:
                    self.pointer += 3
            elif opcode == 7:  # less than
                a, b, target = self.get_indices(3)
                self.intcode[target] = int(self.intcode[a] < self.intcode[b])
                self.pointer += 4
            elif opcode == 8:  # equals
                a, b, target = self.get_indices(3)
                self.intcode[target] = int(self.intcode[a] == self.intcode[b])
                self.pointer += 4
            elif opcode == 9:  # change relative base
                self.relative_base += self.intcode[self.get_indices(1)[0]]
                self.pointer += 2
            else:
                raise ValueError(f"invalid opcode: {opcode}")
        return self.out_value

    def get_indices(self, n):
        self.params += [0] * (n - len(self.params))
        indices = []
        for i, p in enumerate(self.params):
            if p == 0:  # position_mode
                position = self.intcode[self.pointer + i + 1]
            elif p == 1:  # immediate_mode
                position = self.pointer + i + 1
            elif p == 2:  # relative_mode
                position = self.intcode[self.pointer + i + 1] + self.relative_base
            else:
                raise ValueError(f"unknown parameter mode: {p}")
            indices.append(position)
        return indices
