# https://adventofcode.com/2019/day/21


from intcode import IntcodeComputer


with open("day_21_input.txt") as file:
    code = [int(i) for i in file.read().split(",")]
droid = IntcodeComputer(code, silent=True, feedback_mode=True, ascii_mode=True)


def run_droid(instructions=None):
    output = [droid.run(instructions)]
    while not droid.has_halted:
        try:
            output.append(droid.run())
        except (AttributeError, IndexError):
            break
    return "".join(x for x in output if x is not None)


# Catch the output and print only the final numbers.

# part 1
droid_output = run_droid()
# print(droid_output)  # Droid asks for input.
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
droid_output = run_droid(springscript_1)
# print(droid_output)
print(droid_output.splitlines()[-1])  # 19362259


# part 2
droid.reset()
droid_output = run_droid()
# print(droid_output)
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
droid_output = run_droid(springscript_2)
# print(droid_output)
print(droid_output.splitlines()[-1])  # 1141066762
