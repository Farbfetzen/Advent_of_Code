# https://adventofcode.com/2020/day/22

from collections import deque
from copy import deepcopy
from itertools import islice

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2020Day22(Solution):

    def solve(self, inputs: Inputs) -> None:
        decks = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(decks))
        self.sample_results_2.append(self.solve_2(decks))

        decks = self.prepare(inputs.input)
        self.result_1 = self.solve_1(decks)
        self.result_2 = self.solve_2(decks)

    @staticmethod
    def prepare(data: str) -> list[deque[int]]:
        return [deque([int(card) for card in deck.splitlines()[1:]]) for deck in data.split("\n\n")]

    @staticmethod
    def calculate_score(cards: deque[int]) -> int:
        return sum(i * v for i, v in enumerate(reversed(cards), start=1))

    def solve_1(self, decks: list[deque[int]]) -> int:
        decks = deepcopy(decks)
        while True:
            p0 = decks[0].popleft()
            p1 = decks[1].popleft()
            if p0 > p1:
                decks[0].extend((p0, p1))
                if len(decks[1]) == 0:
                    return self.calculate_score(decks[0])
            else:
                decks[1].extend((p1, p0))
                if len(decks[0]) == 0:
                    return self.calculate_score(decks[1])

    def solve_2(self, decks: list[deque[int]], return_index=False) -> int:  # noqa:S3776
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
                winner_round = self.solve_2([new_deck_p0, new_deck_p1], True)
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

        return winner_game if return_index else self.calculate_score(decks[winner_game])
