# https://adventofcode.com/2019/day/5


class IntcodeComputer:
    position_mode = "0"
    immediate_mode = "1"

    def __init__(self, intcode):
        self.intcode = intcode
        self.pointer = 0
        self.params = ""
        self.opcodes = {
            1: self.add,
            2: self.mult,
            3: self.read,
            4: self.print
        }

    def run(self):
        while True:
            instruction = str(self.intcode[self.pointer])
            opcode = int(instruction[-2:])
            self.params = instruction[-3::-1]
            if opcode == 99:
                break
            else:
                self.opcodes[opcode]()

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
        self.intcode[target_position] = int(input("enter an integer: "))
        self.pointer += 2

    def print(self):
        print(self.get_values(1)[0])
        self.pointer += 2


with open("day_05_input.txt", "r") as file:
    program = [int(i) for i in file.read().split(",")]
computer = IntcodeComputer(program)
computer.run()

# Solution of part 1: 9006673
