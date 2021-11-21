# https://adventofcode.com/2019/day/22


CUT = "cut"
DEAL_INTO_NEW_STACK = "deal into new stack"
DEAL_WITH_INCREMENT = "deal with increment"


class Deck:

    def __init__(self, size):
        self.cards = list(range(size))
        self.instruction_map = {
            DEAL_INTO_NEW_STACK: self.deal_into_new_stack,
            CUT: self.cut,
            DEAL_WITH_INCREMENT: self.deal_with_increment
        }

    def shuffle(self, instructions):
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
        if line == DEAL_INTO_NEW_STACK:
            instructions.append((DEAL_INTO_NEW_STACK, None))
        elif line.startswith(CUT):
            instructions.append((CUT, int(line[4:])))
        elif line.startswith(DEAL_WITH_INCREMENT):
            instructions.append((DEAL_WITH_INCREMENT, int(line[20:])))
    return instructions


def test_run(deck_size, instructions):
    deck = Deck(deck_size)
    deck.shuffle(instructions)
    return deck.cards


def part_1(instructions):
    deck = Deck(10_007)
    deck.shuffle(instructions)
    return deck.cards.index(2019)


def part_2(instructions):
    """
    I would have never solved this without the help from these two reources:
    https://www.reddit.com/r/adventofcode/comments/ee56wh/2019_day_22_part_2_so_whats_the_purpose_of_this/fbr0vjb
    https://github.com/nibarius/aoc/blob/master/src/main/aoc2019/Day22.kt
    """
    n_cards = 119315717514047
    n_repetitions = 101741582076661
    instructions = InstructionSimplifier(instructions, n_cards, n_repetitions).simplify()
    index_of_2020 = 2020
    for instruction, n in instructions:
        if instruction == CUT:
            index_of_2020 = (index_of_2020 - n) % n_cards
        elif instruction == DEAL_WITH_INCREMENT:
            index_of_2020 = (index_of_2020 * n) % n_cards
        else:
            index_of_2020 = n_cards - 1 - index_of_2020
    return index_of_2020


class InstructionSimplifier:

    def __init__(self, instructions, n_cards, n_repetitions):
        self.instructions = instructions.copy()
        self.n_cards = n_cards
        self.n_repetitions_left = n_cards - 1 - n_repetitions

    def simplify(self):
        self.reduce()
        result = []
        for x in reversed(bin(self.n_repetitions_left)[2:]):
            if x == "1":
                result.extend(self.instructions)
            self.instructions += self.instructions
            self.reduce()
        self.instructions = result
        self.reduce()
        return self.instructions

    def reduce(self):
        """Reduce the number of instructions."""
        done = False
        while not done:
            done = True
            i = 0
            j = i + 1
            while j < len(self.instructions):
                if self.combine(i, j):
                    done = False
                    continue
                if self.reorder(i, j):
                    done = False
                i += 1
                j += 1

    def combine(self, i, j):
        a, x = self.instructions[i]
        b, y = self.instructions[i + 1]
        if a == DEAL_INTO_NEW_STACK and b == DEAL_INTO_NEW_STACK:
            # Reversing the deck twice is the same as doing nothing.
            del self.instructions[j]
            del self.instructions[i]
        elif a == CUT and b == CUT:
            self.instructions[i] = (CUT, (x + y) % self.n_cards)
            del self.instructions[j]
        elif a == DEAL_WITH_INCREMENT and b == DEAL_WITH_INCREMENT:
            self.instructions[i] = (DEAL_WITH_INCREMENT, (x * y) % self.n_cards)
            del self.instructions[j]
        else:
            return False
        return True

    def reorder(self, i, j):
        a, x = self.instructions[i]
        b, y = self.instructions[i + 1]
        if a == DEAL_INTO_NEW_STACK and b == CUT:
            self.instructions[i] = (CUT, self.n_cards - y)
            self.instructions[i + 1] = (DEAL_INTO_NEW_STACK, None)
        elif a == CUT and b == DEAL_WITH_INCREMENT:
            self.instructions[i] = (DEAL_WITH_INCREMENT, y)
            self.instructions[j] = (CUT, (x * y) % self.n_cards)
        elif a == DEAL_INTO_NEW_STACK and b == DEAL_WITH_INCREMENT:
            self.instructions[i] = (DEAL_WITH_INCREMENT, y)
            self.instructions[j] = (CUT, -(y - 1))
            self.instructions.insert(j + 1, (DEAL_INTO_NEW_STACK, None))
        else:
            return False
        return True


with open("day_22_sample.txt") as file:
    sample_inputs = file.read().split("\n\n")
assert test_run(10, parse_input(sample_inputs[0])) == [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]
assert test_run(10, parse_input(sample_inputs[1])) == [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]
assert test_run(10, parse_input(sample_inputs[2])) == [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]
assert test_run(10, parse_input(sample_inputs[3])) == [9, 2, 5, 8, 1, 4, 7, 0, 3, 6]


with open("day_22_input.txt") as file:
    challenge_input = parse_input(file.read())
print(part_1(challenge_input))  # 2480
print(part_2(challenge_input))  # 62416301438548
