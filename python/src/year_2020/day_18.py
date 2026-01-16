# https://adventofcode.com/2020/day/18

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2020Day18(Solution):

    def solve(self, inputs: Inputs) -> None:
        for sample in inputs.samples:
            homework = self.prepare(sample)
            self.sample_results_1.append(self.solve_1(homework))
            self.sample_results_2.append(self.solve_2(homework))

        homework = self.prepare(inputs.input)
        self.result_1 = self.solve_1(homework)
        self.result_2 = self.solve_2(homework)

    @staticmethod
    def prepare(data: str) -> list[list[int | str]]:
        parsed_data = []
        for line in data.splitlines():
            line = line.replace(" ", "")
            tokens: list[int | str] = []
            for char in line:
                tokens.append(int(char) if char.isdigit() else char)
            parsed_data.append(tokens)
        return parsed_data

    def evaluate(self, expressions: list[int | str], i=0) -> tuple[int, int]:
        left = expressions[i]
        if left == "(":
            left, i = self.evaluate(expressions, i + 1)
        next_i = None
        while i < len(expressions) - 1:
            operator = expressions[i + 1]
            if operator == ")":
                return left, i + 1
            right = expressions[i + 2]
            if right == "(":
                right, next_i = self.evaluate(expressions, i + 3)
            if operator == "+":
                left += right
            elif operator == "*":
                left *= right
            if next_i is None:
                i += 2
            else:
                i = next_i
                next_i = None
        return left, 0

    @staticmethod
    def add_parentheses(line: list[int | str]) -> list[int | str]:
        # Put parentheses around additions so they are evaluated first.
        parentheses_levels = {"(": 1, ")": -1}
        i = 0
        while i < len(line):
            if line[i] != "+":
                i += 1
                continue
            level = 0

            # look left of the "+"
            for j, char in reversed(list(enumerate(line[:i]))):
                level += parentheses_levels.get(char, 0)
                if level == 0:
                    line = line[:j] + ["("] + line[j:]
                    i += 1
                    break

            # look right of the "+"
            for j, char in enumerate(line[i + 1 :], i + 1):
                level += parentheses_levels.get(char, 0)
                if level == 0:
                    line = line[: j + 1] + [")"] + line[j + 1 :]
                    i += 1
                    break

            i += 1
        return line

    def solve_1(self, homework: list[list[int | str]]) -> int:
        return sum(self.evaluate(line)[0] for line in homework)

    def solve_2(self, homework: list[list[int | str]]) -> int:
        return sum(self.evaluate(self.add_parentheses(line))[0] for line in homework)
