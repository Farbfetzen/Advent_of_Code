# https://adventofcode.com/2020/day/24


import collections


# Using axial coordinates:
# https://www.redblobgames.com/grids/hexagons/#coordinates-axial
# Where x runs left to right and y runs north-west to south-east.
# The hexagons are layed out such that the top and bottom are pointy.
DIRECTIONS = {
    "e": (1, 0),
    "se": (0, 1),
    "sw": (-1, 1),
    "w": (-1, 0),
    "nw": (0, -1),
    "ne": (1, -1)
}


def parse_input(input_txt):
    paths = []
    for line in input_txt.splitlines():
        steps = []
        line = list(reversed(line))
        while line:
            direction = line.pop()
            if direction not in "ew":
                direction += line.pop()
            steps.append(DIRECTIONS[direction])
        paths.append(steps)
    return paths


def part_1(paths):
    hexmap = collections.defaultdict(bool)
    for path in paths:
        tile = (0, 0)
        for step in path:
            tile = (tile[0] + step[0], tile[1] + step[1])
        # Only the last tile in a path gets flipped.
        hexmap[tile] = not hexmap[tile]
    return sum(hexmap.values()), hexmap


def check_neighbors(position, old_state, new_state,
                    neighbors_to_check_around=None):
    x, y = position
    n_neighbors = 0
    for dx, dy in DIRECTIONS.values():
        neighbor_position = (x + dx, y + dy)
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
    test_input = parse_input(file.read())
sum_black, tile_map = part_1(test_input)
assert sum_black == 10
assert part_2(tile_map) == 2208


with open("day_24_input.txt") as file:
    challenge_input = parse_input(file.read())
sum_black, tile_map = part_1(challenge_input)
print(sum_black)  # 528
print(part_2(tile_map))  # 4200
