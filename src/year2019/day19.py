# https://adventofcode.com/2019/day/19


from pprint import pprint
from intcode import IntcodeComputer


def part_1():
    n = 0
    beam = []
    for y in range(50):
        row = []
        for x in range(50):
            affected = computer.run((x, y))
            computer.reset()
            row.append(affected)
        n += sum(row)
        beam.append(row)
    return n, beam


def part_2(beam):
    # This works by tracking the bottom-left edge of the beam.
    # Start at the leftmost affected position in the bottom row from part 1.
    # If a hit is detected, check the space diagonally opposite of the square.
    # If that hits, too, then the square fits.
    # If not, go down once, then go right until the next hit is detected.
    y = len(beam) - 1
    x = next(i for i, x in enumerate(beam[y]) if x)
    while True:
        y += 1
        while True:
            computer.reset()
            if computer.run((x, y)):
                break
            x += 1
        computer.reset()
        if computer.run((x + 99, y - 99)):
            return x * 10000 + y - 99


with open("../../input/2019-19-input.txt") as file:
    challenge_input = [int(x) for x in file.read().split(",")]
computer = IntcodeComputer(challenge_input, silent=True)

# part 1
n_affected, beam_map = part_1()
print(n_affected)  # 173

# beam_image = "\n".join(("".join(str(char) for char in b) for b in beam_map))
# print(beam_image)

# part 2
print(part_2(beam_map))  # 6671097
