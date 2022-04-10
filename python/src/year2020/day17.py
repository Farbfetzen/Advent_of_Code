# https://adventofcode.com/2020/day/17

# I implemented it in a way such that the reactor should be able to run
# in any number of dimensions > 1. I tested 2, 3, 4, and 5.

from itertools import product
from operator import add

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[str]:
    return data.splitlines()


def check_neighbors(position, old_state, new_state, directions,
                    candidates=None):
    neighbor_positions = {tuple(map(add, position, direction)) for direction in directions}
    n_neighbors = len(neighbor_positions & old_state)
    active = position in old_state
    if active and n_neighbors in {2, 3} or not active and n_neighbors == 3:
        new_state.add(position)
    if candidates is not None:
        candidates.update(neighbor_positions)


def run_reactor(input_list, n_dim):
    reactor_state = set()
    extra_coordinates = [0] * (n_dim - 2)
    for y, row in enumerate(input_list):
        for x, char in enumerate(row):
            if char == "#":
                position = tuple([x, y] + extra_coordinates)
                reactor_state.add(position)

    directions = list(product((-1, 0, 1), repeat=n_dim))
    directions.remove(tuple([0] * n_dim))

    for _ in range(6):
        new_state = set()
        candidates = set()
        for position in reactor_state:
            check_neighbors(position, reactor_state, new_state, directions,
                            candidates)
        # Check the neighbors of the active cells:
        for position in candidates:
            check_neighbors(position, reactor_state, new_state, directions)
        reactor_state = new_state
    return len(reactor_state)


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(run_reactor(sample_data, 3))
    solution.samples_part_2.append(run_reactor(sample_data, 4))

    challenge_data = prepare_data(data.input)
    solution.part_1 = run_reactor(challenge_data, 3)
    solution.part_2 = run_reactor(challenge_data, 4)
    return solution

    # Not required, but I was curious:
    # print(run_reactor(challenge_input, 2))  # 30
    # print(run_reactor(challenge_input, 5))  # 10632 (takes about a minute)
