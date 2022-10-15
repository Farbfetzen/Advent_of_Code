# https://adventofcode.com/2021/day/4

from src.util.types import Data, Solution


class BingoBoard:

    def __init__(self, numbers):
        self.numbers = [int(n) for n in numbers.replace("\n", " ").split()]
        self.marked = set()

    def mark(self, n):
        if n in self.numbers:
            self.marked.add(n)
            return self.check_win(n)
        return False

    def get_score(self):
        return sum(set(self.numbers).difference(self.marked))

    def check_win(self, n):
        """Check if n completes the row or column it's in."""
        i = self.numbers.index(n)
        r = i // 5 * 5
        c = i % 5
        return (
            self.marked.issuperset(self.numbers[r:r+5])
            or self.marked.issuperset(self.numbers[c::5])
        )


def prepare_data(data: str) -> tuple[list[int], list[BingoBoard]]:
    data_numbers, *data_boards = data.split("\n\n")
    numbers = [int(n) for n in data_numbers.split(",")]
    boards = [BingoBoard(board) for board in data_boards]
    return numbers, boards


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
    raise RuntimeError("Should have returned a result.")


def solve(data: Data) -> Solution:
    sample_data = prepare_data(data.samples[0])
    sample_part_1, sample_part_2 = play(*sample_data)

    challenge_data = prepare_data(data.input)
    challenge_part_1, challenge_part_2 = play(*challenge_data)

    return Solution(
        samples_part_1=[sample_part_1],
        samples_part_2=[sample_part_2],
        part_1=challenge_part_1,
        part_2=challenge_part_2
    )
