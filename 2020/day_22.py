# https://adventofcode.com/2020/day/22


import collections


def parse_input(input_txt):
    decks = []
    for deck in input_txt.split("\n\n"):
        deck = [int(card) for card in deck.splitlines()[1:]]
        decks.append(collections.deque(deck))
    return decks


def part_1(decks):
    winner = None
    while winner is None:
        a = decks[0].popleft()
        b = decks[1].popleft()
        if a > b:
            decks[0].extend((a, b))
            if len(decks[1]) == 0:
                winner = decks[0]
        else:
            decks[1].extend((b, a))
            if len(decks[0]) == 0:
                winner = decks[1]
    winner.reverse()
    score = 0
    for i, v in enumerate(winner, start=1):
        score += i * v
    return score


def part_2(foo):
    return 0


test_input = """\
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""
test_decks = parse_input(test_input)
assert part_1(test_decks) == 306
# assert part_2(test_input) ==


with open("day_22_input.txt") as file:
    challenge_decks = parse_input(file.read())
print(part_1(challenge_decks))  # 30138
# print(part_2(challenge_input))  #
