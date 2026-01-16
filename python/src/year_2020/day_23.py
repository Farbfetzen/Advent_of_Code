# https://adventofcode.com/2020/day/23

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2020Day23(Solution):

    def solve(self, inputs: Inputs) -> None:
        cups = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(cups))
        self.sample_results_2.append(self.solve_2(cups))

        cups = self.prepare(inputs.input)
        self.result_1 = self.solve_1(cups)
        self.result_2 = self.solve_2(cups)

    @staticmethod
    def prepare(data: str) -> list[int]:
        return [int(x) for x in data]

    @staticmethod
    def play(cups: list[int], n_moves: int, n_cups: int) -> list[int]:
        """The list next_cups acts as a linked list where next_cups[c] points to the right neighbor of c."""
        current_cup = cups[0]
        cups = cups + list(range(len(cups) + 1, n_cups + 1))
        next_cups = [0] * (n_cups + 1)
        for i, c in enumerate(cups):
            next_cups[c] = cups[(i + 1) % n_cups]
        for _ in range(n_moves):
            removed_1st = next_cups[current_cup]
            removed_2nd = next_cups[removed_1st]
            removed_3rd = next_cups[removed_2nd]
            destination = current_cup
            while True:
                destination -= 1
                if destination < 1:
                    destination = n_cups
                if destination not in (removed_1st, removed_2nd, removed_3rd):
                    break
            next_cups[current_cup] = current_cup = next_cups[removed_3rd]
            next_cups[removed_3rd] = next_cups[destination]
            next_cups[destination] = removed_1st
        return next_cups

    def solve_1(self, cups: list[int]) -> int:
        linked_cups = self.play(cups, 100, len(cups))
        result = ""
        current = 1
        for _ in range(len(cups) - 1):
            current = linked_cups[current]
            result += str(current)
        return int(result)

    def solve_2(self, cups: list[int]) -> int:
        linked_cups = self.play(cups, 10_000_000, 1_000_000)
        a = linked_cups[1]
        b = linked_cups[a]
        return a * b
