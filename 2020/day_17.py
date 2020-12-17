# https://adventofcode.com/2020/day/17


import itertools


def run_reactor(input_txt, n_dimensions):
    directions = list(itertools.product((-1, 0, 1), repeat=4))
    directions.remove((0, 0, 0, 0))

    initial_state = {}
    z = w = 0
    for y, row in enumerate(input_txt.splitlines()):
        for x, char in enumerate(row):
            if char == "#":
                initial_state[(x, y, z, w)] = True
    # Add the neighbors of the active cells:
    for (x, y, z, w), value in initial_state.copy().items():
        for dx, dy, dz, dw in directions:
            if n_dimensions == 3 and dw != 0:
                continue
            neighbor_position = (x + dx, y + dy, z + dz, w + dw)
            if neighbor_position not in initial_state:
                initial_state[neighbor_position] = False

    reactor_state = initial_state.copy()
    for _ in range(6):
        new_state = reactor_state.copy()
        protected = set()
        for (x, y, z, w), value in reactor_state.items():
            n_neighbors = 0
            for dx, dy, dz, dw in directions:
                if n_dimensions == 3 and dw != 0:
                    continue
                n_neighbors += reactor_state.get((x+dx, y+dy, z+dz, w+dw), 0)
            if n_neighbors == 0 and (x, y, z, w) not in protected:
                # Remove cells with no neighbors to reduce the size of the dict.
                del new_state[(x, y, z, w)]
            elif value and n_neighbors not in (2, 3):
                new_state[(x, y, z, w)] = False
            elif not value and n_neighbors == 3:
                new_state[(x, y, z, w)] = True
                # Also add all neighbors around the newly active cell:
                for dx, dy, dz, dw in directions:
                    if n_dimensions == 3 and dw != 0:
                        continue
                    neighbor_position = (x+dx, y+dy, z+dz, w+dw)
                    protected.add(neighbor_position)
                    if neighbor_position not in new_state:
                        new_state[neighbor_position] = False
        reactor_state = new_state
    return sum(reactor_state.values())


test_input = """\
.#.
..#
###
"""
assert run_reactor(test_input, 3) == 112
assert run_reactor(test_input, 4) == 848

with open("day_17_input.txt") as file:
    challenge_input = file.read()
print(run_reactor(challenge_input, 3))  # 232
print(run_reactor(challenge_input, 4))  # 1620
