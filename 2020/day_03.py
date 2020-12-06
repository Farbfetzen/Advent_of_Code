# https://adventofcode.com/2020/day/3


import math


def convert_input(input_str):
    return [[x == "#" for x in line] for line in input_str.splitlines()]


def check_slope(data, slope):
    width = len(data[0])
    height = len(data)
    right, down = slope
    x = right % width
    y = down
    n_trees = 0
    while y < height:
        n_trees += data[y][x]
        x = (x + right) % width
        y += down
    return n_trees


test_input = convert_input("""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""")
assert check_slope(test_input, (3, 1)) == 7


with open("day_03_input.txt") as file:
    tree_map = convert_input(file.read())

# part 1:
print(check_slope(tree_map, (3, 1)))  # 211

# part 2:
slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
print(math.prod(check_slope(tree_map, slope) for slope in slopes))  # 3584591857
