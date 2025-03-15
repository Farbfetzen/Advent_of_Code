# https://adventofcode.com/2020/day/20

from math import sqrt

import numpy

from src.util.inputs import Inputs
from src.util.solution import Solution


class Tile:

    def __init__(self, data) -> None:
        data = data.splitlines()
        self.id = int(data[0][5:-1])
        self.content = numpy.array([list(line) for line in data[1:]])
        self.borders = {
            self.top,
            self.bottom,
            self.left,
            self.right
        }
        self.rotate(2)
        self.borders.update((
            self.top,
            self.bottom,
            self.left,
            self.right
        ))
        self.shared_borders = set()
        self.neighbors = set()
        self.n_neighbors = 0

    def rotate(self, n=1) -> None:
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
            for other in tiles[i + 1:]:
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

    # noinspection PyUnboundLocalVariable
    @staticmethod
    def solve_2(tiles: list[Tile]) -> int:
        # Find a corner tile for the top left corner.
        for tile in tiles:
            if tile.n_neighbors == 2:
                break
        # Rotate until the shared borders are bottom and right.
        for _ in range(4):
            if {tile.right, tile.bottom}.issubset(tile.shared_borders):
                break
            tile.rotate()

        # first row of whole image
        tile_map = [[tile]]
        side_length = int(sqrt(len(tiles)))
        for i in range(1, side_length):
            for neighbor in tile.neighbors:
                if tile.right in neighbor.shared_borders:
                    break
            for j in range(8):
                if neighbor.left == tile.right:
                    break
                neighbor.rotate()
                if j == 4:
                    neighbor.flip()
            tile_map[0].append(neighbor)
            tile = neighbor

        # all other rows
        for y in range(1, side_length):
            row = []
            for x in range(side_length):
                tile = tile_map[y - 1][x]
                for neighbor in tile.neighbors:
                    if tile.bottom in neighbor.shared_borders:
                        break
                for j in range(8):
                    if neighbor.top == tile.bottom:
                        break
                    neighbor.rotate()
                    if j == 4:
                        neighbor.flip()
                row.append(neighbor)
            tile_map.append(row)

        size = tile.content.shape[0] - 2
        image_size = side_length * size
        image = numpy.empty(shape=(image_size, image_size), dtype=str)

        for y, row in enumerate(tile_map):
            for x, tile in enumerate(row):
                image[y * size:(y + 1) * size, x * size:(x + 1) * size] = tile.content[1:-1, 1:-1]

        monster = numpy.array((
            list("                  # "),
            list("#    ##    ##    ###"),
            list(" #  #  #  #  #  #   ")
        ))
        monster_pos = {(x, y) for y, x in zip(*numpy.where(monster == "#"))}
        monster_width = len(monster[0])
        monster_height = len(monster)

        monster_found = False
        for i in range(8):
            # Rough water positions need to be calculated after every rotation or flip.
            all_rough_water_pos = {(x, y) for y, x in zip(*numpy.where(image == "#"))}
            for y in range(image_size - monster_height):
                for x in range(image_size - monster_width):
                    cropped = image[y:y + monster_height, x:x + monster_width]
                    rough_water_pos = set()
                    for cy, row in enumerate(cropped):
                        for cx, char in enumerate(row):
                            if char == "#":
                                rough_water_pos.add((cx, cy))
                    if monster_pos.issubset(rough_water_pos):
                        monster_found = True
                        for x_, y_ in monster_pos & rough_water_pos:
                            pos = (x + x_, y + y_)
                            all_rough_water_pos.remove(pos)
            if monster_found:
                break
            image = numpy.rot90(image)
            if i == 4:
                image = numpy.flip(image, 1)
        return len(all_rough_water_pos)
