# https://adventofcode.com/2019/day/21


# TODO: Include an ascii mode in the IntcodeComputer.


from intcode import IntcodeComputer


with open("day_21_input.txt") as file:
    code = [int(i) for i in file.read().split(",")]
droid = IntcodeComputer(code, silent=True, feedback_mode=True)


def run_droid(instructions=None):
    # Same hack as in day 17. I still don't know why it keeps breaking.
    output = []
    if instructions is not None:
        instructions = [ord(instr) for instr in instructions]
        if instructions[-1] != 10:  # missing newline
            instructions.append(10)
        output.append(chr(droid.run(instructions)))
    while not droid.has_halted:
        try:
            next_output = droid.run()
        except (AttributeError, IndexError):
            break
        if next_output is not None:
            if next_output <= int(0x10ffff):  # max value for chr()
                next_output = chr(next_output)
            else:
                next_output = str(next_output)
            output.append(next_output)
    return "".join(x for x in output)


def to_ascii(instructions):
    return [ord(instr) for instr in instructions]


# part 1
print(run_droid())  # Droid asks for input.
# Jump if there is a hole at A or B or C but only if there is ground at D.
springscript_1 = """\
NOT B J
NOT C T
OR T J
NOT A T
OR T J
AND D J
WALK
"""
print(run_droid(springscript_1))  # 19362259


# part 2
droid.reset()
print(run_droid())
# Same as in part 1 but there must also be ground at H.
springscript_2 = """\
NOT B J
NOT C T
OR T J
NOT A T
OR T J
AND D J
OR H T
AND T J
RUN
"""
print(run_droid(springscript_2))  # 1141066762
