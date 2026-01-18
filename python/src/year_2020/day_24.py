# https://adventofcode.com/2020/day/24

from src.util.inputs import Inputs
from src.util.solution import Solution


# Using axial coordinates where x runs from left to right and y runs from north-west to south-east.
# I use complex numbers so movement is simply the sum of directions.
# https://www.redblobgames.com/grids/hexagons/#coordinates-axial
DIRECTIONS = {
    "e": 1 + 0j,
    "se": 0 + 1j,
    "sw": -1 + 1j,
    "w": -1 + 0j,
    "nw": 0 - 1j,
    "ne": 1 - 1j,
}


class Solution2020Day24(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = self.prepare(inputs.samples[0])
        sum_black, tiles = self.solve_1(prepared_input)
        self.sample_results_1.append(sum_black)
        self.sample_results_2.append(self.solve_2(tiles))

        prepared_input = self.prepare(inputs.input)
        sum_black, tiles = self.solve_1(prepared_input)
        self.result_1 = sum_black
        self.result_2 = self.solve_2(tiles)

    @staticmethod
    def prepare(data: str) -> list[complex]:
        positions = []
        for line_str in data.splitlines():
            position = 0 + 0j
            line = list(reversed(line_str))
            while line:
                direction = line.pop()
                if direction not in "ew":
                    direction += line.pop()
                position += DIRECTIONS[direction]
            positions.append(position)
        return positions

    @staticmethod
    def solve_1(positions: list[complex]) -> tuple[int, set[complex]]:
        hexmap: set[complex] = set()
        for position in positions:
            hexmap.symmetric_difference_update({position})
        return len(hexmap), hexmap

    @staticmethod
    def check_neighbors(
        position: complex, old_state: set[complex], new_state: set[complex], candidates: set[complex] | None = None
    ) -> None:
        neighbor_positions = {position + direction for direction in DIRECTIONS.values()}
        n_neighbors = len(neighbor_positions & old_state)
        active = position in old_state
        if active and n_neighbors in {1, 2} or not active and n_neighbors == 2:
            new_state.add(position)
        if candidates is not None:
            candidates.update(neighbor_positions)

    def solve_2(self, hexmap: set[complex]) -> int:
        # hexmap stores only the black tiles as a set.
        for _ in range(100):
            new_hexmap: set[complex] = set()
            candidates: set[complex] = set()
            for position in hexmap:
                self.check_neighbors(position, hexmap, new_hexmap, candidates)
            # Check the neighbors of the active cells:
            for position in candidates:
                self.check_neighbors(position, hexmap, new_hexmap)
            hexmap = new_hexmap
        return len(hexmap)
