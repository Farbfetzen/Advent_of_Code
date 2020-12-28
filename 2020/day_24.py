# https://adventofcode.com/2020/day/24


import collections


# Using axial coordinates:
# https://www.redblobgames.com/grids/hexagons/#coordinates-axial
# Where x runs left to right and y runs north-west to south-east.
# The hexagons are layed out such that the top and bottom are pointy.
# I use complex coordinates so movement is simply the sum of directions.
DIRECTIONS = {
    "e": 1+0j,
    "se": 0+1j,
    "sw": -1+1j,
    "w": -1+0j,
    "nw": 0-1j,
    "ne": 1-1j
}


def parse_input(input_txt):
    positions = []
    for line in input_txt.splitlines():
        position = 0
        line = list(reversed(line))
        while line:
            direction = line.pop()
            if direction not in "ew":
                direction += line.pop()
            position += DIRECTIONS[direction]
        positions.append(position)
    return positions


def part_1(positions):
    hexmap = collections.defaultdict(bool)
    for position in positions:
        hexmap[position] = not hexmap[position]
    return sum(hexmap.values()), hexmap


def check_neighbors(position, old_state, new_state,
                    neighbors_to_check_around=None):
    n_neighbors = 0
    for direction in DIRECTIONS.values():
        neighbor_position = position + direction
        n_neighbors += old_state.get(neighbor_position, 0)
        if neighbors_to_check_around is not None:
            neighbors_to_check_around.add(neighbor_position)
    value = old_state.get(position, 0)
    if value and n_neighbors in (1, 2) or not value and n_neighbors == 2:
        new_state[position] = True


def part_2(hexmap):
    for _ in range(100):
        new_hexmap = {}
        neighbors_to_check_around = set()
        for position in hexmap:
            check_neighbors(position, hexmap, new_hexmap,
                            neighbors_to_check_around)
        # Check the neighbors of the active cells:
        for position in neighbors_to_check_around:
            check_neighbors(position, hexmap, new_hexmap)
        hexmap = new_hexmap
    return sum(hexmap.values())


with open("day_24_sample.txt") as file:
    test_positions = parse_input(file.read())
sum_black, test_tiles = part_1(test_positions)
assert sum_black == 10
assert part_2(test_tiles) == 2208


with open("day_24_input.txt") as file:
    challenge_positions = parse_input(file.read())
sum_black, challenge_tiles = part_1(challenge_positions)
print(sum_black)  # 528
print(part_2(challenge_tiles))  # 4200
