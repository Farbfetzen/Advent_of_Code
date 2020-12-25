# https://adventofcode.com/2020/day/20


import math
import numpy


class Tile:
    def __init__(self, data):
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

    def rotate(self, n=1):
        self.content = numpy.rot90(self.content, n)

    def flip(self):
        self.content = numpy.flip(self.content, 1)

    @property
    def top(self):
        return "".join(self.content[0, :])

    @property
    def bottom(self):
        return "".join(self.content[-1, :])

    @property
    def left(self):
        return "".join(self.content[:, 0])

    @property
    def right(self):
        return "".join(self.content[:, -1])


def part_1(tiles):
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


def part_2(tiles):
    # Find a corner tile for the top left corner.
    for tile in tiles:
        if tile.n_neighbors == 2:
            break
    # Rotate until the shared borders are bottom and right.
    for _ in range(4):
        if (tile.right in tile.shared_borders
                and tile.bottom in tile.shared_borders):
            break
        tile.rotate()

    # first row of whole image
    tile_map = [[tile]]
    sidelength = int(math.sqrt(len(tiles)))
    for i in range(1, sidelength):
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
    for y in range(1, sidelength):
        row = []
        for x in range(sidelength):
            tile = tile_map[y-1][x]
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
    image_size = sidelength * size
    image = numpy.empty(shape=(image_size, image_size), dtype=str)

    for y, row in enumerate(tile_map):
        for x, tile in enumerate(row):
            image[y*size:(y+1)*size, x*size:(x+1)*size] = tile.content[1:-1, 1:-1]

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
                cropped = image[y:y+monster_height, x:x+monster_width]
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


with open("day_20_sample.txt") as file:
    test_input = file.read().split("\n\n")
test_tiles = [Tile(data) for data in test_input]
assert part_1(test_tiles) == 20899048083289
assert part_2(test_tiles) == 273

with open("day_20_input.txt") as file:
    challenge_input = file.read().split("\n\n")
challenge_tiles = [Tile(data) for data in challenge_input]
print(part_1(challenge_tiles))  # 27798062994017
print(part_2(challenge_tiles))  # 2366
