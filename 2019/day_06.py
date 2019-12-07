def sum_orbits(orbits):
    total = 0
    for o in orbits:
        while o != "COM":
            o = orbits[o]
            total += 1
    return total


def decode_orbits(orbit_txt):
    orbits = {}
    for line in orbit_txt.split():
        a, b = line.split(")")
        orbits[b] = a
    return orbits


def find_com(orbits, start):
    path = []
    position = orbits[start]
    while position != "COM":
        path.append(position)
        position = orbits[position]
    return path


def go_to_santa(orbits):
    you_to_com = find_com(orbits, "YOU")
    san_to_com = find_com(orbits, "SAN")
    jumps = set(you_to_com).symmetric_difference(san_to_com)
    return len(jumps)


test1 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""
assert sum_orbits(decode_orbits(test1)) == 42
test2 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
"""
assert go_to_santa(decode_orbits(test2)) == 4


with open("day_06_input.txt") as file:
    day_06_input = file.read()

# part 1:
print(sum_orbits(decode_orbits(day_06_input)))  # 253104
# part 2:
print(go_to_santa(decode_orbits(day_06_input)))  # 499
