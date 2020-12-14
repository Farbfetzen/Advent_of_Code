from collections import defaultdict


class IntcodeComputer:
    def __init__(self, intcode, silent=False, feedback_mode=False):
        self.intcode = defaultdict(int, {i: x for i, x in enumerate(intcode)})
        self.original_intcode = self.intcode.copy()
        self.silent = silent
        self.feedback_mode = feedback_mode
        self.inputs = None
        self.pointer = 0
        self.relative_base = 0
        self.has_halted = False
        self.is_paused = False
        self.out_value = None
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
        self.out_value = None

    def get_next_instruction(self):
        instruction = str(self.intcode[self.pointer])
        opcode = int(instruction[-2:])
        parameters = [int(i) for i in instruction[-3::-1]]
        return opcode, parameters

    def run(self, inputs=None):
        if inputs is not None:
            # Reverse input because popping from the end is better.
            self.inputs = list(reversed(inputs))
        self.out_value = None
        self.is_paused = False
        while not (self.has_halted or self.is_paused):
            opcode, parameters = self.get_next_instruction()
            self.opcode_methods[opcode](parameters)
        return self.out_value

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
        self.out_value = self.intcode[position]
        if not self.silent:
            print(self.out_value)
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


if __name__ == "__main__":
    # Check if the IntcodeComputer still works correctly after changing it.
    # Works by catching all the print outputs into a string and comparing it
    # with the expected outputs. This is quick and easy because I don't want to
    # use a proper unittest library here.

    EXPECTED = (
        "3101844",
        "8478",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "9006673",
        "3629692",
        "21000",
        "61379886",
        "2457252183",
        "70634",
        "2428",
        " ███    ██ █    ████ ███  █  █  ██  █  █   ",
        " █  █    █ █    █    █  █ █  █ █  █ █  █   ",
        " █  █    █ █    ███  ███  █  █ █    █  █   ",
        " ███     █ █    █    █  █ █  █ █    █  █   ",
        " █ █  █  █ █    █    █  █ █  █ █  █ █  █   ",
        " █  █  ██  ████ █    ███   ██   ██   ██    ",
        "268",
        "13989",
        "330",
        "352",
        "8520",
        "926819",
        "173",
        "6671097",
        "Input instructions:",
        "",
        "",
        "Walking...",
        "",
        "19362259",
        "Input instructions:",
        "",
        "",
        "Running...",
        "",
        "1141066762",
    )

    # Redirect print() output to a string.
    # Source: https://stackoverflow.com/a/40984270
    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        import day_02
        import day_05
        import day_07
        import day_09
        import day_11
        import day_13
        import day_15
        import day_17
        import day_19
        import day_21
    out = f.getvalue().splitlines()

    ok = True
    for i, line in enumerate(out):
        exp = EXPECTED[i]
        try:
            assert exp == line
        except AssertionError:
            print(f"{line=}")
            print(f"{exp=}\n")
            ok = False
    if ok:
        print("Ok")
    else:
        print("Found some errors.")
