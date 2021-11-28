# https://adventofcode.com/2020/day/18


def get_data(filename, sample=False):
    with open(filename) as file:
        data = file.read()
    if sample:
        return [parse_data(line.splitlines()) for line in data.split("\n\n")]
    return parse_data(data.splitlines())


def parse_data(data):
    parsed_data = []
    for line in data:
        parsed_data.append([int(x) if x.isdigit() else x for x in line.replace(" ", "")])
    return parsed_data


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


sample_data = get_data("day_18_sample.txt", sample=True)
challenge_data = get_data("day_18_input.txt")

if __name__ == "__main__":
    assert part_1(sample_data[0]) == 71
    assert part_1(sample_data[1]) == 51
    assert part_1(sample_data[2]) == 26
    assert part_1(sample_data[3]) == 437
    assert part_1(sample_data[4]) == 12240
    assert part_1(sample_data[5]) == 13632

    assert part_2(sample_data[0]) == 231
    assert part_2(sample_data[1]) == 51
    assert part_2(sample_data[2]) == 46
    assert part_2(sample_data[3]) == 1445
    assert part_2(sample_data[4]) == 669060
    assert part_2(sample_data[5]) == 23340

    print(part_1(challenge_data))  # 25190263477788
    print(part_2(challenge_data))  # 297139939002972
