# https://adventofcode.com/2019/day/4

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2019Day04(Solution):

    def solve(self, inputs: Inputs) -> None:
        self.result_1, self.result_2 = self.count_passwords([int(i) for i in inputs.input.split("-")])

    @staticmethod
    def prepare(data: str) -> list[int]:
        return [int(i) for i in data.split("-")]

    @staticmethod
    def check_increasing_digits(password: str) -> bool:
        return list(password) == sorted(password)

    @staticmethod
    def check_adjacent_pairs(password: str) -> bool:
        return any(x == y for x, y in zip(password, password[1:]))

    @staticmethod
    def check_adjacent_pairs_group(password: str) -> bool:
        return 2 in (password.count(digit) for digit in password)

    def count_passwords(self, password_range: list[int]) -> tuple[int, int]:
        total_part_1 = 0
        total_part_2 = 0
        for password_num in range(password_range[0], password_range[1] + 1):
            password = str(password_num)
            if self.check_increasing_digits(password):
                total_part_1 += self.check_adjacent_pairs(password)
                total_part_2 += self.check_adjacent_pairs_group(password)
        return total_part_1, total_part_2
