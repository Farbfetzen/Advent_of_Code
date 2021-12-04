# https://adventofcode.com/2021/day/4


class BingoBoard:

    def __init__(self, numbers):
        self.numbers = [int(n) for n in numbers.replace("\n", " ").split()]
        self.marked = set()

    def mark(self, n):
        if n in self.numbers:
            self.marked.add(n)
            return self.check_win()
        return False

    def get_score(self):
        return sum(set(self.numbers).difference(self.marked))

    def check_win(self):
        return self.check_rows() or self.check_columns()

    def check_rows(self):
        for i in range(0, 21, 5):
            if self.marked.issuperset(self.numbers[i:i+5]):
                return True
        return False

    def check_columns(self):
        for i in range(5):
            if self.marked.issuperset(self.numbers[i::5]):
                return True
        return False


def get_data(filename):
    with open(filename) as file:
        numbers, *boards = file.read().split("\n\n")
    numbers = [int(n) for n in numbers.split(",")]
    boards = [BingoBoard(board) for board in boards]
    return numbers, boards


def play(numbers, boards):
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


sample_data = get_data("day_04_sample.txt")
challenge_data = get_data("day_04_input.txt")

if __name__ == "__main__":
    sample_part_1, sample_part_2 = play(*sample_data)
    assert sample_part_1 == 4512
    assert sample_part_2 == 1924

    challenge_part_1, challenge_part_2 = play(*challenge_data)
    print(challenge_part_1)  # 23177
    print(challenge_part_2)  # 6804
