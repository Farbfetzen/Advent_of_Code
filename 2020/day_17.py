# https://adventofcode.com/2020/day/17


import itertools


DIRECTIONS = list(itertools.product((-1, 0, 1), repeat=4))
DIRECTIONS.remove((0, 0, 0, 0))


def parse_input(input_txt):
    initial_state = {}
    z = w = 0
    for y, row in enumerate(input_txt.splitlines()):
        for x, char in enumerate(row):
            if char == "#":
                initial_state[(x, y, z, w)] = True
    return initial_state


def check_neighbors(x, y, z, w, value, old_state, new_state, _3d,
                    neighbors_to_check_around=None):
    n_neighbors = 0
    for dx, dy, dz, dw in DIRECTIONS:
        if _3d and dw != 0:
            continue
        neighbor_position = (x + dx, y + dy, z + dz, w + dw)
        n_neighbors += old_state.get(neighbor_position, 0)
        if neighbors_to_check_around is not None:
            neighbors_to_check_around.add(neighbor_position)
    if value and n_neighbors in (2, 3) or not value and n_neighbors == 3:
        new_state[(x, y, z, w)] = True


def run_reactor(initial_state, _3d=True):
    reactor_state = initial_state.copy()
    for _ in range(6):
        new_state = {}
        neighbors_to_check_around = set()
        for (x, y, z, w), value in reactor_state.items():
            check_neighbors(x, y, z, w, value, reactor_state, new_state, _3d,
                            neighbors_to_check_around)
        # Check the neighbors of the active cells:
        for (x, y, z, w) in neighbors_to_check_around:
            check_neighbors(x, y, z, w, reactor_state.get((x, y, z, w), 0),
                            reactor_state, new_state, _3d)
        reactor_state = new_state
    return sum(reactor_state.values())


test_input = """\
.#.
..#
###
"""
test_input = parse_input(test_input)
assert run_reactor(test_input) == 112
assert run_reactor(test_input, False) == 848

challenge_input = parse_input(open("day_17_input.txt").read())
print(run_reactor(challenge_input))  # 232
print(run_reactor(challenge_input, False))  # 1620
