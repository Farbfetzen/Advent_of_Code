from defaultlist import defaultlist


class IntcodeComputer:
    def __init__(self, intcode, silent=False, feedback_mode=False):
        self.original_intcode = defaultlist(int)
        self.original_intcode.extend(intcode)
        self.intcode = self.original_intcode.copy()
        self.silent = silent
        self.feedback_mode = feedback_mode
        self.inputs = None
        self.pointer = 0
        self.relative_base = 0
        self.has_halted = False

    def reset(self):
        self.intcode = self.original_intcode.copy()
        self.pointer = 0
        self.relative_base = 0
        self.has_halted = False

    def get_next_instruction(self):
        instruction = str(self.intcode[self.pointer])
        opcode = int(instruction[-2:])
        params = [int(i) for i in instruction[-3::-1]]
        return opcode, params

    def run(self, inputs=None):
        if inputs is not None:
            # reverse input because popping from the right end is better
            self.inputs = list(reversed(inputs))
        out_value = None
        while True:
            opcode, params = self.get_next_instruction()
            if opcode == 1:  # add
                a, b, target = self.get_indices(params, 3)
                self.intcode[target] = self.intcode[a] + self.intcode[b]
                self.pointer += 4
            elif opcode == 2:  # mult
                a, b, target = self.get_indices(params, 3)
                self.intcode[target] = self.intcode[a] * self.intcode[b]
                self.pointer += 4
            elif opcode == 3:  # read
                self.intcode[self.get_indices(params, 1)[0]] = self.inputs.pop()
                self.pointer += 2
            elif opcode == 4:  # print or return
                out_value = self.intcode[self.get_indices(params, 1)[0]]
                if not self.silent:
                    print(out_value)
                self.pointer += 2
                if self.get_next_instruction()[0] == 99:
                    # Return one step early to try to avoid returning None.
                    self.has_halted = True
                    break
                if self.feedback_mode:
                    break
            elif opcode == 5:  # jump if True
                i, target = self.get_indices(params, 2)
                if self.intcode[i] != 0:
                    self.pointer = self.intcode[target]
                else:
                    self.pointer += 3
            elif opcode == 6:  # jump if False
                i, target = self.get_indices(params, 2)
                if self.intcode[i] == 0:
                    self.pointer = self.intcode[target]
                else:
                    self.pointer += 3
            elif opcode == 7:  # less than
                a, b, target = self.get_indices(params, 3)
                self.intcode[target] = int(self.intcode[a] < self.intcode[b])
                self.pointer += 4
            elif opcode == 8:  # equals
                a, b, target = self.get_indices(params, 3)
                self.intcode[target] = int(self.intcode[a] == self.intcode[b])
                self.pointer += 4
            elif opcode == 9:  # change relative base
                self.relative_base += self.intcode[self.get_indices(params, 1)[0]]
                self.pointer += 2
            elif opcode == 99:
                self.has_halted = True
                break
            else:
                raise ValueError(f"invalid opcode: {opcode}")
        return out_value

    def get_indices(self, params, n):
        params += [0] * (n - len(params))
        indices = []
        for i, p in enumerate(params):
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
