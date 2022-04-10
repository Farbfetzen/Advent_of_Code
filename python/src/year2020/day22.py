# https://adventofcode.com/2020/day/22

from collections import deque
from copy import deepcopy
from itertools import islice

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[deque[int]]:
    return [deque([int(card) for card in deck.splitlines()[1:]])
            for deck in data.split("\n\n")]


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


def part_2(decks, return_index=False):
    cache = set()
    winner_game = None
    while winner_game is None:
        d = (tuple(decks[0]), tuple(decks[1]))
        if d in cache:
            winner_game = 0  # player 1 (= index 0) wins
            break
        cache.add(d)
        p0 = decks[0].popleft()
        p1 = decks[1].popleft()
        if p0 <= len(decks[0]) and p1 <= len(decks[1]):
            new_deck_p0 = deque(islice(decks[0], 0, p0))
            new_deck_p1 = deque(islice(decks[1], 0, p1))
            winner_round = part_2([new_deck_p0, new_deck_p1], True)
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

    if return_index:
        return winner_game
    else:
        return calculate_score(decks[winner_game])


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
