# https://adventofcode.com/2020/day/18

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[list[int | str]]:
    parsed_data = []
    for line in data.splitlines():
        line = line.replace(" ", "")
        tokens: list[int | str] = []
        for char in line:
            tokens.append(int(char) if char.isdigit() else char)
        parsed_data.append(tokens)
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


def solve(data: Data) -> Solution:
    solution = Solution()
    for i in range(6):
        sample_data = prepare_data(data.samples[i])
        solution.samples_part_1.append(part_1(sample_data))
        solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
