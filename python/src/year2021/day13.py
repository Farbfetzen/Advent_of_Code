# https://adventofcode.com/2021/day/13

from typing import NamedTuple

from src.util.types import Data, Point2, Solution


Fold = NamedTuple("Fold", (("index", bool), ("value", int)))


def prepare_data(data: str) -> tuple[set[Point2], list[Fold]]:
    top, bottom = data.split("\n\n")
    points = set()
    for line in top.splitlines():
        x, y = line.split(",")
        points.add(Point2(int(x), int(y)))
    folds = []
    for line in bottom.splitlines():
        along, value = line.split("=")
        fold = Fold(along[-1] == "y", int(value))
        folds.append(fold)
    return points, folds


def fold_once(points, fold):
    new_points = set()
    for point in points:
        if point[fold.index] > fold.value:
            p = list(point)
            p[fold.index] = fold.value - (point[fold.index] - fold.value)
            point = Point2(*p)
        new_points.add(point)
    return new_points


def part_1(points, folds):
    points = fold_once(points, folds[0])
    return len(points)


def part_2(points, folds):
    for fold in folds:
        points = fold_once(points, fold)
    len_horizontal = max(points, key=lambda p: p.x).x + 1
    len_vertical = max(points, key=lambda p: p.y).y + 1
    code = [[" "] * len_horizontal for _ in range(len_vertical)]
    for point in points:
        code[point.y][point.x] = "█"
    return "\n".join("".join(line) for line in code)


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(*sample_data))
    solution.samples_part_2.append(part_2(*sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(*challenge_data)
    solution.part_2 = part_2(*challenge_data)
    return solution
