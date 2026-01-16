# https://adventofcode.com/2021/day/4

from src.util.exceptions import ResultExpectedError
from src.util.inputs import Inputs
from src.util.solution import Solution


class BingoBoard:

    def __init__(self, numbers: str) -> None:
        self.numbers = [int(n) for n in numbers.replace("\n", " ").split()]
        self.marked = set()

    def mark(self, n: int) -> bool:
        if n in self.numbers:
            self.marked.add(n)
            return self.check_win(n)
        return False

    def get_score(self) -> int:
        return sum(set(self.numbers).difference(self.marked))

    def check_win(self, n: int) -> bool:
        """Check if n completes the row or column it's in."""
        i = self.numbers.index(n)
        r = i // 5 * 5
        c = i % 5
        return self.marked.issuperset(self.numbers[r : r + 5]) or self.marked.issuperset(self.numbers[c::5])


class Solution2021Day04(Solution):

    def solve(self, inputs: Inputs) -> None:
        numbers, boards = self.prepare(inputs.samples[0])
        sample_result_1, sample_result_2 = self.play(numbers, boards)
        self.sample_results_1.append(sample_result_1)
        self.sample_results_2.append(sample_result_2)

        numbers, boards = self.prepare(inputs.input)
        self.result_1, self.result_2 = self.play(numbers, boards)

    @staticmethod
    def prepare(data: str) -> tuple[list[int], list[BingoBoard]]:
        data_numbers, *data_boards = data.split("\n\n")
        numbers = [int(n) for n in data_numbers.split(",")]
        boards = [BingoBoard(board) for board in data_boards]
        return numbers, boards

    @staticmethod
    def play(numbers: list[int], boards: list[BingoBoard]) -> tuple[int, int]:
        winning_score = None
        for n in numbers:
            boards_to_remove = set()
            for board in boards:
                if board.mark(n):
                    boards_to_remove.add(board)
                    if winning_score is None:
                        winning_score = board.get_score() * n
                    elif len(boards) == 1:
                        losing_score = board.get_score() * n
                        return winning_score, losing_score
            boards = [board for board in boards if board not in boards_to_remove]
        raise ResultExpectedError
