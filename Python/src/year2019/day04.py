# https://adventofcode.com/2019/day/4

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[int]:
    return [int(i) for i in data.split("-")]


def check_increasing_digits(password: str) -> bool:
    return list(password) == sorted(password)


def check_adjacent_pairs(password: str) -> bool:
    return any(x == y for x, y in zip(password, password[1:]))


def check_adjacent_pairs_group(password: str) -> bool:
    return 2 in (password.count(digit) for digit in password)


def count_passwords(password_range: list[int]) -> tuple[int, int]:
    total_part_1 = 0
    total_part_2 = 0
    for password_num in range(password_range[0], password_range[1] + 1):
        password = str(password_num)
        if check_increasing_digits(password):
            total_part_1 += check_adjacent_pairs(password)
            total_part_2 += check_adjacent_pairs_group(password)
    return total_part_1, total_part_2


def solve(data: Data) -> Solution:
    solution = Solution()
    challenge_data = prepare_data(data.input)
    solution.part_1, solution.part_2 = count_passwords(challenge_data)
    return solution
