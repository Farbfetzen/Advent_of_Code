# https://adventofcode.com/2019/day/6


def decode_orbits(orbit_txt):
    orbits = {}
    for line in orbit_txt.split():
        a, b = line.split(")")
        orbits[b] = a
    return orbits


def sum_orbits(orbits):
    total = 0
    for o in orbits:
        total += len(find_com(orbits, o)) + 1
    return total


def find_com(orbits, start):
    path = []
    position = orbits[start]
    while position != "COM":
        path.append(position)
        position = orbits[position]
    return path


def jumps_to_santa(orbits):
    you_to_com = find_com(orbits, "YOU")
    san_to_com = find_com(orbits, "SAN")
    jumps = set(you_to_com).symmetric_difference(san_to_com)
    return len(jumps)


with open("../../input/2019-06-sample.txt") as file:
    test_inputs = file.read().split("\n\n")
test1 = test_inputs[0]
assert sum_orbits(decode_orbits(test1)) == 42
test2 = test_inputs[1]
assert jumps_to_santa(decode_orbits(test2)) == 4


with open("../../input/2019-06-input.txt") as file:
    day_06_input = file.read()

# part 1:
print(sum_orbits(decode_orbits(day_06_input)))  # 253104
# part 2:
print(jumps_to_santa(decode_orbits(day_06_input)))  # 499
