# https://adventofcode.com/2020/day/20

import itertools
from math import sqrt

import numpy

from src.util.exceptions import ResultExpectedError
from src.util.inputs import Inputs
from src.util.solution import Solution


class Tile:

    def __init__(self, data: str) -> None:
        lines = data.splitlines()
        self.id = int(lines[0][5:-1])
        self.content = numpy.array([list(line) for line in lines[1:]])
        self.borders = {self.top, self.bottom, self.left, self.right}
        self.rotate(2)
        self.borders.update((self.top, self.bottom, self.left, self.right))
        self.shared_borders: set[str] = set()
        self.neighbors: set[Tile] = set()
        self.n_neighbors = 0

    def rotate(self, n: int = 1) -> None:
        self.content = numpy.rot90(self.content, n)

    def flip(self) -> None:
        self.content = numpy.flip(self.content, 1)

    @property
    def top(self) -> str:
        return "".join(self.content[0, :])

    @property
    def bottom(self) -> str:
        return "".join(self.content[-1, :])

    @property
    def left(self) -> str:
        return "".join(self.content[:, 0])

    @property
    def right(self) -> str:
        return "".join(self.content[:, -1])


class Solution2020Day20(Solution):

    def solve(self, inputs: Inputs) -> None:
        tiles = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(tiles))
        self.sample_results_2.append(self.solve_2(tiles))

        tiles = self.prepare(inputs.input)
        self.result_1 = self.solve_1(tiles)
        self.result_2 = self.solve_2(tiles)

    @staticmethod
    def prepare(data: str) -> list[Tile]:
        return [Tile(t) for t in data.split("\n\n")]

    @staticmethod
    def solve_1(tiles: list[Tile]) -> int:
        for i, tile in enumerate(tiles[:-1]):
            for other in tiles[i + 1 :]:
                shared_borders = tile.borders & other.borders
                if shared_borders:
                    tile.neighbors.add(other)
                    other.neighbors.add(tile)
                    tile.shared_borders.update(shared_borders)
                    other.shared_borders.update(shared_borders)
        corner_product = 1
        for tile in tiles:
            tile.n_neighbors = len(tile.neighbors)
            if tile.n_neighbors == 2:
                corner_product *= tile.id
        return corner_product

    def solve_2(self, tiles: list[Tile]) -> int:
        tile = self.find_corner_tile(tiles)
        self.rotate_align(tile)
        tile_map = [[tile]]
        side_length = int(sqrt(len(tiles)))
        self.assemble_first_row(tile, tile_map, side_length)
        self.assemble_other_rows(tile_map, side_length)

        size = tile.content.shape[0] - 2
        image_size = side_length * size
        image = numpy.empty(shape=(image_size, image_size), dtype=str)

        for y, row in enumerate(tile_map):
            for x, tile in enumerate(row):
                image[y * size : (y + 1) * size, x * size : (x + 1) * size] = tile.content[1:-1, 1:-1]

        monster = numpy.array(
            (
                list("                  # "),
                list("#    ##    ##    ###"),
                list(" #  #  #  #  #  #   "),
            )
        )
        monster_height, monster_width = monster.shape
        monster_pos = {(x, y) for y, x in zip(*numpy.nonzero(monster == "#"))}
        all_rough_water_pos = self.find_rough_water(monster_width, monster_height, monster_pos, image, image_size)
        return len(all_rough_water_pos)

    @staticmethod
    def find_corner_tile(tiles: list[Tile]) -> Tile:
        """Find a corner tile for the top left corner."""
        for tile in tiles:
            if tile.n_neighbors == 2:
                return tile
        raise ResultExpectedError

    @staticmethod
    def rotate_align(tile: Tile) -> None:
        """Rotate until the shared borders are bottom and right."""
        for _ in range(4):
            if {tile.right, tile.bottom}.issubset(tile.shared_borders):
                break
            tile.rotate()

    @staticmethod
    def assemble_first_row(tile: Tile, tile_map: list[list[Tile]], side_length: int) -> None:
        """First row of whole image."""
        for _ in range(1, side_length):
            neighbor = next(neighbor for neighbor in tile.neighbors if tile.right in neighbor.shared_borders)
            for j in range(8):
                if neighbor.left == tile.right:
                    break
                neighbor.rotate()
                if j == 4:
                    neighbor.flip()
            tile_map[0].append(neighbor)
            tile = neighbor

    @staticmethod
    def assemble_other_rows(tile_map: list[list[Tile]], side_length: int) -> None:
        """All other rows of the image."""
        for y in range(1, side_length):
            row = []
            for x in range(side_length):
                tile = tile_map[y - 1][x]
                neighbor = next(neighbor for neighbor in tile.neighbors if tile.bottom in neighbor.shared_borders)
                for j in range(8):
                    if neighbor.top == tile.bottom:
                        break
                    neighbor.rotate()
                    if j == 4:
                        neighbor.flip()
                row.append(neighbor)
            tile_map.append(row)

    @staticmethod
    def find_rough_water(
        monster_width: int,
        monster_height: int,
        monster_pos: set[tuple[int, int]],
        image: numpy.ndarray,
        image_size: int,
    ) -> set[tuple[int, int]]:
        monster_found = False
        for i in range(8):
            # Rough water positions need to be calculated after every rotation or flip.
            all_rough_water_pos = {(x, y) for y, x in zip(*numpy.nonzero(image == "#"))}
            for x, y in itertools.product(range(image_size - monster_width), range(image_size - monster_height)):
                cropped = image[y : y + monster_height, x : x + monster_width]
                rough_water_pos = {
                    (cx, cy) for cy, row in enumerate(cropped) for cx, char in enumerate(row) if char == "#"
                }
                if monster_pos.issubset(rough_water_pos):
                    monster_found = True
                    for x_, y_ in monster_pos & rough_water_pos:
                        pos = (x + x_, y + y_)
                        all_rough_water_pos.remove(pos)
            if monster_found:
                return all_rough_water_pos
            image = numpy.rot90(image)
            if i == 4:
                image = numpy.flip(image, 1)
        raise ResultExpectedError
