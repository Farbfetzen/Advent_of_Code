# https://adventofcode.com/2019/day/22


class Deck:
    def __init__(self, size):
        self.cards = list(range(size))
        self.instruction_map = {
            "deal into new stack": self.deal_into_new_stack,
            "cut": self.cut,
            "deal with increment": self.deal_with_increment
        }

    def run(self, instructions):
        for instruction, argument in instructions:
            self.instruction_map[instruction](argument)

    def deal_into_new_stack(self, _):
        self.cards.reverse()

    def cut(self, n):
        self.cards[-n:], self.cards[:-n] = self.cards[:n], self.cards[n:]

    def deal_with_increment(self, step_size):
        new_cards = [0] * len(self.cards)
        for i, x in enumerate(self.cards):
            new_cards[(i * step_size) % len(self.cards)] = x
        self.cards = new_cards


def parse_input(input_txt):
    instructions = []
    for line in input_txt.splitlines():
        if line == "deal into new stack":
            instructions.append(("deal into new stack", None))
        elif line.startswith("cut"):
            instructions.append(("cut", int(line[4:])))
        elif line.startswith("deal with increment"):
            instructions.append(("deal with increment", int(line[20:])))
    return instructions


def test_run(deck_size, instructions):
    deck = Deck(deck_size)
    deck.run(instructions)
    return deck.cards


def part_1(instructions):
    deck = Deck(10_007)
    deck.run(instructions)
    return deck.cards.index(2019)


def part_2(instructions):
    # No.
    # TODO: Look into the solutions and try to implement one in my own words.
    # https://www.reddit.com/r/adventofcode/comments/ee56wh/2019_day_22_part_2_so_whats_the_purpose_of_this/fbr0vjb
    # https://www.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions
    # https://www.reddit.com/r/adventofcode/comments/eh1d6p/2019_day_22_part_2_tutorial
    pass


with open("day_22_sample.txt") as file:
    test_inputs = file.read().split("\n\n")
assert test_run(10, parse_input(test_inputs[0])) == [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]
assert test_run(10, parse_input(test_inputs[1])) == [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]
assert test_run(10, parse_input(test_inputs[2])) == [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]
assert test_run(10, parse_input(test_inputs[3])) == [9, 2, 5, 8, 1, 4, 7, 0, 3, 6]


with open("day_22_input.txt") as file:
    challenge_input = parse_input(file.read())
print(part_1(challenge_input))  # 2480
# print(part_2(challenge_input))  #
