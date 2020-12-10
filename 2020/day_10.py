# https://adventofcode.com/2020/day/10


def part_1(adapters):
    adapters.append(0)
    adapters.sort()
    differences = [adapters[i + 1] - x for i, x in enumerate(adapters[:-1])]
    # +1 for the difference to the device
    return differences.count(1) * (differences.count(3) + 1)


def part_2(adapters):
    # Requires that part_1() ran before because the adapters must be sorted
    # and they must include 0.
    possibilities = {adapters[-1]: 1}
    for a in reversed(adapters[:-1]):
        possibilities[a] = sum(possibilities.get(x, 0) for x in (a+1, a+2, a+3))
    return possibilities[0]


test_input_1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
assert part_1(test_input_1) == 7 * 5
assert part_2(test_input_1) == 8
test_input_2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38,
                39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
assert part_1(test_input_2) == 22 * 10
assert part_2(test_input_2) == 19208

with open("day_10_input.txt") as file:
    challenge_input = [int(x) for x in file.read().splitlines()]
print(part_1(challenge_input))  # 2760
print(part_2(challenge_input))  # 13816758796288
