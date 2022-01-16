# https://adventofcode.com/2019/day/6


SAMPLE_PATH = "../../input/2019-06-sample.txt"
INPUT_PATH = "../../input/2019-06-input.txt"


def get_data(filename):
    with open(filename) as file:
        return file.read().split("\n\n")


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


def part_1(orbits):
    total = 0
    for o in orbits:
        total += len(find_com(orbits, o)) + 1
    return total


def part_2(orbits):
    you_to_com = find_com(orbits, "YOU")
    san_to_com = find_com(orbits, "SAN")
    jumps = set(you_to_com).symmetric_difference(san_to_com)
    return len(jumps)


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(decode_orbits(sample_data[0])) == 42
    assert part_2(decode_orbits(sample_data[1])) == 4

    challenge_data = decode_orbits(get_data(INPUT_PATH)[0])
    print(part_1(challenge_data))  # 253104
    print(part_2(challenge_data))  # 499
