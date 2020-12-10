# https://adventofcode.com/2020/day/10


def part_1(adapters):
    adapters.append(0)
    adapters.sort()
    n_diff_1 = 0
    n_diff_3 = 1  # start with 1 for the difference to the device
    for i, x in enumerate(adapters[:-1]):
        difference = adapters[i + 1] - x
        if difference == 1:
            n_diff_1 += 1
        elif difference == 3:
            n_diff_3 += 1
    return n_diff_1 * n_diff_3


def part_2(adapters):
    adapters.sort()
    possibilities = {adapters[-1]: 1}
    for i, a in reversed(list(enumerate(adapters[:-1]))):
        choices = []
        for b in adapters[(i + 1):]:
            if b - a <= 3:
                choices.append(b)
            else:
                break
        possibilities[a] = sum(possibilities[c] for c in choices)
    return possibilities[0]


test_input_1 = """16
10
15
5
1
11
7
19
6
12
4
""".splitlines()
test_input_1 = [int(x) for x in test_input_1]
assert part_1(test_input_1) == 7 * 5
assert part_2(test_input_1) == 8
test_input_2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
""".splitlines()
test_input_2 = [int(x) for x in test_input_2]
assert part_1(test_input_2) == 22 * 10
assert part_2(test_input_2) == 19208

with open("day_10_input.txt") as file:
    challenge_input = [int(x) for x in file.read().splitlines()]
print(part_1(challenge_input))  # 2760
print(part_2(challenge_input))  # 13816758796288
