# https://adventofcode.com/2020/day/3


import math


def get_data(filename):
    with open(filename) as file:
        data = file.read()
    return [[x == "#" for x in line] for line in data.splitlines()]


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


def part_1(map_of_trees):
    return check_slope(map_of_trees, (3, 1))


def part_2(map_of_trees):
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    n_trees = (check_slope(map_of_trees, slope) for slope in slopes)
    return math.prod(n_trees)


sample_data = get_data("../../input/2020-03-sample.txt")
challenge_data = get_data("../../input/2020-03-input.txt")

if __name__ == "__main__":
    assert part_1(sample_data) == 7

    print(part_1(challenge_data))  # 211
    print(part_2(challenge_data))  # 3584591857
