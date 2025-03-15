# https://adventofcode.com/2020/day/17

import itertools
import operator

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2020Day17(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = inputs.samples[0].splitlines()
        self.sample_results_1.append(self.run_reactor(prepared_input, 3))
        self.sample_results_2.append(self.run_reactor(prepared_input, 4))

        prepared_input = inputs.input.splitlines()
        self.result_1 = self.run_reactor(prepared_input, 3)
        self.result_2 = self.run_reactor(prepared_input, 4)

        # Not required, but I was curious:
        # print(self.run_reactor(prepared_input, 2))  # 30
        # print(self.run_reactor(prepared_input, 5))  # 10632 (takes about a minute)

    @staticmethod
    def check_neighbors(position, old_state, new_state, directions, candidates=None) -> None:
        neighbor_positions = {tuple(map(operator.add, position, direction)) for direction in directions}
        n_neighbors = len(neighbor_positions & old_state)
        active = position in old_state
        if active and n_neighbors in {2, 3} or not active and n_neighbors == 3:
            new_state.add(position)
        if candidates is not None:
            candidates.update(neighbor_positions)

    def run_reactor(self, input_list: list[str], n_dim: int) -> int:
        reactor_state = set()
        extra_coordinates = [0] * (n_dim - 2)
        for y, row in enumerate(input_list):
            for x, char in enumerate(row):
                if char == "#":
                    position = tuple([x, y] + extra_coordinates)
                    reactor_state.add(position)

        directions = list(itertools.product((-1, 0, 1), repeat=n_dim))
        directions.remove(tuple([0] * n_dim))

        for _ in range(6):
            new_state = set()
            candidates = set()
            for position in reactor_state:
                self.check_neighbors(position, reactor_state, new_state, directions,
                                     candidates)
            # Check the neighbors of the active cells:
            for position in candidates:
                self.check_neighbors(position, reactor_state, new_state, directions)
            reactor_state = new_state
        return len(reactor_state)
