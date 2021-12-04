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
        return sum(self.marked.symmetric_difference(self.numbers))

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
        data = file.read().split("\n\n")
    drawn_numbers = [int(n) for n in data[0].split(",")]
    # Reverse the list because popping from the right is better.
    drawn_numbers.reverse()
    boards = [BingoBoard(numbers) for numbers in data[1:]]
    return drawn_numbers, boards


def part_1(numbers, boards):
    winning_board = None
    while numbers:
        n = numbers.pop()
        for board in boards:
            if board.mark(n):
                winning_board = board
        if winning_board is not None:
            boards.remove(winning_board)
            return winning_board.get_score() * n


def part_2(numbers, boards):
    while numbers:
        n = numbers.pop()
        boards_to_remove = set()
        for board in boards:
            win = board.mark(n)
            if win:
                if len(boards) > 1:
                    boards_to_remove.add(board)
                else:
                    return board.get_score() * n
        boards = [board for board in boards if board not in boards_to_remove]


sample_data = get_data("day_04_sample.txt")
challenge_data = get_data("day_04_input.txt")

if __name__ == "__main__":
    assert part_1(*sample_data) == 4512
    assert part_2(*sample_data) == 1924

    print(part_1(*challenge_data))  # 23177
    print(part_2(*challenge_data))  # 6804

# Parts 1 and 2 are connected because they mutate the data. That's why in part 1 all boards
# have to be marked with a number before it can return or else some boards will miss a mark
# in part 2. The benefit of this approach is that in part 2 the boards are already partially
# marked, so I don't have to start at the beginning.
