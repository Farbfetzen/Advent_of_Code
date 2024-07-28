# https://adventofcode.com/2020/day/2

from typing import NamedTuple

from src.util.types import Data, Solution


class PasswordEntry(NamedTuple):

    min: int
    max: int
    letter: str
    password: str


def prepare_data(data: str) -> list[PasswordEntry]:
    password_entries = []
    for line in data.strip().splitlines():
        entry = line.split()
        i, j = entry[0].split("-")
        password_entries.append(PasswordEntry(int(i), int(j), entry[1][0], entry[2]))
    return password_entries


def part_1(password_data):
    sum_valid = 0
    for password_entry in password_data:
        letter_count = password_entry.password.count(password_entry.letter)
        if password_entry.min <= letter_count <= password_entry.max:
            sum_valid += 1
    return sum_valid


def part_2(password_data):
    sum_valid = 0
    for password_entry in password_data:
        a = password_entry.password[password_entry.min - 1] == password_entry.letter
        b = password_entry.password[password_entry.max - 1] == password_entry.letter
        if a != b:
            sum_valid += 1
    return sum_valid


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
