# https://adventofcode.com/2020/day/2

from typing import NamedTuple

from src.util.inputs import Inputs
from src.util.solution import Solution


class PasswordEntry(NamedTuple):
    min: int
    max: int
    letter: str
    password: str


class Solution2020Day02(Solution):

    def solve(self, inputs: Inputs) -> None:
        password_data = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(password_data))
        self.sample_results_2.append(self.solve_2(password_data))

        password_data = self.prepare(inputs.input)
        self.result_1 = self.solve_1(password_data)
        self.result_2 = self.solve_2(password_data)

    @staticmethod
    def prepare(data: str) -> list[PasswordEntry]:
        password_entries = []
        for line in data.strip().splitlines():
            entry = line.split()
            i, j = entry[0].split("-")
            password_entries.append(PasswordEntry(int(i), int(j), entry[1][0], entry[2]))
        return password_entries

    @staticmethod
    def solve_1(password_data: list[PasswordEntry]) -> int:
        sum_valid = 0
        for password_entry in password_data:
            letter_count = password_entry.password.count(password_entry.letter)
            if password_entry.min <= letter_count <= password_entry.max:
                sum_valid += 1
        return sum_valid

    @staticmethod
    def solve_2(password_data: list[PasswordEntry]) -> int:
        sum_valid = 0
        for password_entry in password_data:
            a = password_entry.password[password_entry.min - 1] == password_entry.letter
            b = password_entry.password[password_entry.max - 1] == password_entry.letter
            if a != b:
                sum_valid += 1
        return sum_valid
