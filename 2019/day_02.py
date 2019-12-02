# https://adventofcode.com/2019/day/2


def run_intcode(program):
	program = program.copy()
	i = 0
	opcode = program[i]
	while opcode != 99:
		pos_a = program[i+1]
		pos_b = program[i+2]
		target_pos = program[i+3]
		if program[i] == 1:
			program[target_pos] = program[pos_a] + program[pos_b]
		elif program[i] == 2:
			program[target_pos] = program[pos_a] * program[pos_b]
		else:
			raise ValueError("unexpected integer")
		i += 4
		opcode = program[i]
	return(program[0])


with open("day_02_input.txt", "r") as file:
	program = [int(i) for i in file.read().split(",")]


# part 1
program[1] = 12
program[2] = 2
result = run_intcode(program)
print(result)


# part 2
target = 19690720
for noun in range(100):
	for verb in range(100):
		program[1] = noun
		program[2] = verb
		try:
			result = run_intcode(program)
		except:
			continue
		if result == target:
			break
	else:
		continue
	break
print(100 * noun + verb)
