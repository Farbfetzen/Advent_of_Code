# https://adventofcode.com/2020/day/22


from collections import deque
from itertools import islice
from copy import deepcopy


def parse_input(input_txt):
    decks = []
    for deck in input_txt.split("\n\n"):
        deck = [int(card) for card in deck.splitlines()[1:]]
        decks.append(deque(deck))
    decks = tuple(decks)
    return decks


def calculate_score(cards):
    return sum(i * v for i, v in enumerate(reversed(cards), start=1))


def part_1(decks):
    decks = deepcopy(decks)
    while True:
        p0 = decks[0].popleft()
        p1 = decks[1].popleft()
        if p0 > p1:
            decks[0].extend((p0, p1))
            if len(decks[1]) == 0:
                return calculate_score(decks[0])
        else:
            decks[1].extend((p1, p0))
            if len(decks[0]) == 0:
                return calculate_score(decks[1])


def play_recursive(decks, top_level=False):
    cache = set()
    winner_game = None
    while winner_game is None:
        d = (tuple(decks[0]), tuple(decks[1]))
        if d in cache:
            return 0  # player 1 (= index 0) wins
        else:
            cache.add(d)
        p0 = decks[0].popleft()
        p1 = decks[1].popleft()
        if p0 <= len(decks[0]) and p1 <= len(decks[1]):
            new_deck = [
                deque(islice(decks[0], 0, p0)),
                deque(islice(decks[1], 0, p1))
            ]
            winner_round = play_recursive(new_deck)
        elif p0 > p1:
            winner_round = 0
        else:
            winner_round = 1
        if winner_round == 0:
            decks[0].extend((p0, p1))
            if len(decks[1]) == 0:
                winner_game = 0
        else:
            decks[1].extend((p1, p0))
            if len(decks[0]) == 0:
                winner_game = 1

    if top_level:
        return decks[winner_game]
    else:
        return winner_game


def part_2(decks):
    winner = play_recursive(deepcopy(decks), True)
    return calculate_score(winner)


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
assert part_2(test_decks) == 291

with open("day_22_input.txt") as file:
    challenge_decks = parse_input(file.read())
print(part_1(challenge_decks))  # 30138
print(part_2(challenge_decks))  # 31587
