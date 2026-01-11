# https://adventofcode.com/2021/day/18

import copy
import itertools
from math import ceil, floor
from typing import Self

from src.util.inputs import Inputs
from src.util.solution import Solution


class SnailfishNumber:

    def __init__(
            self,
            value: int | None = None,
            parent: Self | None = None,
            left: Self | None = None,
            right: Self | None = None
    ) -> None:
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        if self.value is None:
            return f"[{repr(self.left)},{repr(self.right)}]"
        else:
            return repr(self.value)

    @property
    def magnitude(self) -> int:
        if self.value is None:
            return 3 * self.left.magnitude + 2 * self.right.magnitude
        return self.value


class Solution2021Day18(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(prepared_input))
        self.sample_results_2.append(self.solve_2(prepared_input))

        prepared_input = self.prepare(inputs.input)
        self.result_1 = self.solve_1(prepared_input)
        self.result_2 = self.solve_2(prepared_input)

    def prepare(self, data: str) -> list[SnailfishNumber]:
        return [self.construct_number(line) for line in data.splitlines()]

    def solve_1(self, numbers: list[SnailfishNumber]) -> int:
        current = numbers[0]
        for next_number in numbers[1:]:
            current = self.add(current, next_number)
        return current.magnitude

    def solve_2(self, numbers: list[SnailfishNumber]) -> int:
        max_magnitude = 0
        for a, b in itertools.permutations(numbers, 2):
            max_magnitude = max(self.add(a, b).magnitude, max_magnitude)
        return max_magnitude

    @staticmethod
    def construct_number(input_str: str) -> SnailfishNumber:
        root = SnailfishNumber()
        current = root
        for char in input_str:
            if char == "[":
                current.left = SnailfishNumber(parent=current)
                current.right = SnailfishNumber(parent=current)
                current = current.left
            elif char == "]":
                current = current.parent
            elif char == ",":
                current = current.parent.right
            else:
                # The rest are single digits.
                current.value = int(char)
        return root

    def add(self, left, right) -> SnailfishNumber:
        left = copy.deepcopy(left)
        right = copy.deepcopy(right)
        number = SnailfishNumber(left=left, right=right)
        left.parent = number
        right.parent = number
        while True:
            number_to_explode = self.find_explosion_candidate(number)
            if number_to_explode is not None:
                self.explode(number_to_explode)
            else:
                number_to_split = self.find_split_candidate(number)
                if number_to_split is not None:
                    self.split(number_to_split)
                else:
                    break
        return number

    def find_explosion_candidate(self, number: SnailfishNumber, depth=0) -> SnailfishNumber | None:
        if number.value is None:
            if depth == 4:
                return number
            depth += 1
            return self.find_explosion_candidate(number.left, depth) or \
                self.find_explosion_candidate(number.right, depth)
        return None

    def find_split_candidate(self, number: SnailfishNumber, depth=0) -> SnailfishNumber | None:
        assert number is not None
        if number.value is None:
            depth += 1
            return self.find_split_candidate(number.left, depth) or \
                self.find_split_candidate(number.right, depth)
        if number.value >= 10:
            return number
        return None

    @staticmethod
    def explode(number: SnailfishNumber) -> None:
        # left side:
        current = number
        while current.parent.left == current:
            current = current.parent
            if current.parent is None:
                break
        else:
            current = current.parent.left
            while current.value is None:
                current = current.right
            current.value += number.left.value

        # right side:
        current = number
        while current.parent.right == current:
            current = current.parent
            if current.parent is None:
                break
        else:
            current = current.parent.right
            while current.value is None:
                current = current.left
            current.value += number.right.value

        number.left = None
        number.right = None
        number.value = 0

    @staticmethod
    def split(number: SnailfishNumber) -> None:
        half = number.value / 2
        number.left = SnailfishNumber(value=floor(half), parent=number)
        number.right = SnailfishNumber(value=ceil(half), parent=number)
        number.value = None
