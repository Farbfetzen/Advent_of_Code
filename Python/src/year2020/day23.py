# https://adventofcode.com/2020/day/23

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[int]:
    return [int(x) for x in data]


def play(cups, n_moves, n_cups):
    """The list next_cup acts as a linked list
    where next_cup[c] points to the right neighbor of c."""
    current_cup = cups[0]
    cups = cups + list(range(len(cups) + 1, n_cups + 1))
    next_cup = [0] * (n_cups + 1)
    for i, c in enumerate(cups):
        next_cup[c] = cups[(i + 1) % n_cups]
    for _ in range(n_moves):
        removed_1st = next_cup[current_cup]
        removed_2nd = next_cup[removed_1st]
        removed_3rd = next_cup[removed_2nd]
        destination = current_cup
        while True:
            destination -= 1
            if destination < 1:
                destination = n_cups
            if destination not in (removed_1st, removed_2nd, removed_3rd):
                break
        next_cup[current_cup] = current_cup = next_cup[removed_3rd]
        next_cup[removed_3rd] = next_cup[destination]
        next_cup[destination] = removed_1st
    return next_cup


def part_1(cups):
    linked_cups = play(cups, 100, len(cups))
    result = ""
    current = 1
    for _ in range(len(cups) - 1):
        current = linked_cups[current]
        result += str(current)
    return result


def part_2(cups):
    linked_cups = play(cups, 10_000_000, 1_000_000)
    a = linked_cups[1]
    b = linked_cups[a]
    return str(a * b)


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
