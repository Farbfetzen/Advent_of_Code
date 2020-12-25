# https://adventofcode.com/2020/day/20


import collections
import itertools
import math
import numpy
from pprint import pprint


class Tile:
    def __init__(self, data):
        data = data.splitlines()
        self.id = int(data[0][5:-1])
        self.content = numpy.array([list(line) for line in data[1:]])
        self.edges = {  # all edges, forward and backward
            "".join(self.content[:, 0]),
            "".join(self.content[::-1, 0]),
            "".join(self.content[:, -1]),
            "".join(self.content[::-1, -1]),
            "".join(self.content[0, :]),
            "".join(self.content[0, ::-1]),
            "".join(self.content[-1, :]),
            "".join(self.content[-1, ::-1])
        }
        self.neighbors = set()
        self.n_neighbors = 0
        # print(self.id)
        # print(self.content)
        # print(self.edges)

    def rotate(self):
        pass

    def flip(self):
        pass


def part_1(tiles):
    for i, tile in enumerate(tiles[:-1]):
        for other in tiles[i + 1:]:
            if tile.edges & other.edges:
                tile.neighbors.add(other)
                other.neighbors.add(tile)
    corner_product = 1
    for tile in tiles:
        tile.n_neighbors = len(tile.neighbors)
        if tile.n_neighbors == 2:
            corner_product *= tile.id
    return corner_product


def part_2(foo):
    return 0


with open("day_20_sample.txt") as file:
    test_input = file.read().split("\n\n")
test_tiles = [Tile(data) for data in test_input]
assert part_1(test_tiles) == 20899048083289
# assert part_2(test_input) ==


with open("day_20_input.txt") as file:
    challenge_input = file.read().split("\n\n")
challenge_tiles = [Tile(data) for data in challenge_input]
print(part_1(challenge_tiles))  # 27798062994017
# print(part_2(challenge_input))  #
