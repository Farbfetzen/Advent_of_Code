# https://adventofcode.com/2020/day/24

from src.util.types import Data, Solution


# Using axial coordinates:
# https://www.redblobgames.com/grids/hexagons/#coordinates-axial
# Where x runs left to right and y runs north-west to south-east.
# I use complex numbers so movement is simply the sum of directions.
DIRECTIONS = {
    "e": 1+0j,
    "se": 0+1j,
    "sw": -1+1j,
    "w": -1+0j,
    "nw": 0-1j,
    "ne": 1-1j
}


def prepare_data(data: str) -> list[complex]:
    positions = []
    for line_str in data.splitlines():
        position = 0+0j
        line = list(reversed(line_str))
        while line:
            direction = line.pop()
            if direction not in "ew":
                direction += line.pop()
            position += DIRECTIONS[direction]
        positions.append(position)
    return positions


def part_1(positions):
    hexmap = set()
    for position in positions:
        hexmap.symmetric_difference_update({position})
    return len(hexmap), hexmap


def check_neighbors(position, old_state, new_state,
                    candidates=None):
    neighbor_positions = {position + direction for direction in DIRECTIONS.values()}
    n_neighbors = len(neighbor_positions & old_state)
    active = position in old_state
    if active and n_neighbors in {1, 2} or not active and n_neighbors == 2:
        new_state.add(position)
    if candidates is not None:
        candidates.update(neighbor_positions)


def part_2(hexmap):
    # hexmap stores only the black tiles as a set.
    for _ in range(100):
        new_hexmap = set()
        candidates = set()
        for position in hexmap:
            check_neighbors(position, hexmap, new_hexmap, candidates)
        # Check the neighbors of the active cells:
        for position in candidates:
            check_neighbors(position, hexmap, new_hexmap)
        hexmap = new_hexmap
    return len(hexmap)


def solve(data: Data) -> Solution:
    sample_data = prepare_data(data.samples[0])
    sample_sum_black, sample_tiles = part_1(sample_data)

    challenge_data = prepare_data(data.input)
    challenge_sum_black, challenge_tiles = part_1(challenge_data)

    return Solution(
        samples_part_1=[sample_sum_black],
        samples_part_2=[part_2(sample_tiles)],
        part_1=challenge_sum_black,
        part_2=part_2(challenge_tiles)
    )
