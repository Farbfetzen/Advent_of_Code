# https://adventofcode.com/2019/day/21


from intcode import IntcodeComputer


with open("../../input/2019-21-input.txt") as file:
    code = [int(i) for i in file.read().split(",")]
droid = IntcodeComputer(code, silent=True, feedback_mode=True, ascii_mode=True)

# Catch the output and print only the final numbers.

# part 1
droid_output = droid.run_ascii()
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
droid_output = droid.run_ascii(springscript_1)
# print(droid_output)
print(droid_output.splitlines()[-1])  # 19362259


# part 2
droid.reset()
droid_output = droid.run_ascii()
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
droid_output = droid.run_ascii(springscript_2)
# print(droid_output)
print(droid_output.splitlines()[-1])  # 1141066762
