# https://adventofcode.com/2020/day/5

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[int]:
    return [get_seat_id(p) for p in sorted(data.splitlines())]


def get_seat_id(boarding_pass):
    # No need to separate rows from columns because the "row * 8" is
    # automatically handled if I treat the boarding pass as a 10 digit
    # binary number.
    binary_pass = "".join("1" if x in "BR" else "0" for x in boarding_pass)
    return int(binary_pass, 2)


def part_1(ids):
    return max(ids)


def part_2(ids):
    for i, id_ in enumerate(ids):
        if ids[i + 1] - id_ == 2:
            return id_ + 1


def solve(data: Data) -> Solution:
    solution = Solution()
    solution.samples_other = {"seat ids": [get_seat_id(s) for s in data.samples]}

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
