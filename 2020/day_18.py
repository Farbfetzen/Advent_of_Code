# https://adventofcode.com/2020/day/18


def parse_input(input_str):
    data = []
    for line in input_str.splitlines():
        data.append([int(x) if x.isdigit() else x
                     for x in list(line.replace(" ", ""))])
    return data


def evaluate(expressions, i=0):
    left = expressions[i]
    if left == "(":
        left, i = evaluate(expressions, i + 1)
    next_i = None
    while i < len(expressions) - 1:
        operator = expressions[i + 1]
        if operator == ")":
            return left, i + 1
        right = expressions[i + 2]
        if right == "(":
            right, next_i = evaluate(expressions, i + 3)
        if operator == "+":
            left += right
        elif operator == "*":
            left *= right
        if next_i is None:
            i += 2
        else:
            i = next_i
            next_i = None
    return left


def part_1(homework):
    return sum(evaluate(line) for line in homework)


def add_parentheses(line):
    # Put parentheses around additions so they are evaluated first.
    parentheses_levels = {"(": 1, ")": -1}
    i = 0
    while i < len(line):
        if line[i] == "+":
            level = 0
            # look left of the "+"
            for j, char in reversed(list(enumerate(line[:i]))):
                level += parentheses_levels.get(char, 0)
                if level == 0:
                    line = line[:j] + ["("] + line[j:]
                    i += 1
                    break
            # look right of the "+"
            for j, char in enumerate(line[i + 1:], i + 1):
                level += parentheses_levels.get(char, 0)
                if level == 0:
                    line = line[:j+1] + [")"] + line[j+1:]
                    i += 1
                    break
        i += 1
    return line


def part_2(homework):
    return sum(evaluate(add_parentheses(line)) for line in homework)


test_input_1 = parse_input("1 + 2 * 3 + 4 * 5 + 6")
test_input_2 = parse_input("1 + (2 * 3) + (4 * (5 + 6))")
test_input_3 = parse_input("2 * 3 + (4 * 5)")
test_input_4 = parse_input("5 + (8 * 3 + 9 + 3 * 4 * 3)")
test_input_5 = parse_input("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")
test_input_6 = parse_input("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")

assert part_1(test_input_1) == 71
assert part_1(test_input_2) == 51
assert part_1(test_input_3) == 26
assert part_1(test_input_4) == 437
assert part_1(test_input_5) == 12240
assert part_1(test_input_6) == 13632

assert part_2(test_input_1) == 231
assert part_2(test_input_2) == 51
assert part_2(test_input_3) == 46
assert part_2(test_input_4) == 1445
assert part_2(test_input_5) == 669060
assert part_2(test_input_6) == 23340

with open("day_18_input.txt") as file:
    challenge_input = parse_input(file.read())
print(part_1(challenge_input))  # 25190263477788
print(part_2(challenge_input))  # 297139939002972
