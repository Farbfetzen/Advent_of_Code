# https://adventofcode.com/2021/day/13

from typing import NamedTuple

from src.util.inputs import Inputs
from src.util.solution import Solution
from src.util.util import Point2


Fold = NamedTuple("Fold", (("index", bool), ("value", int)))


class Solution2021Day13(Solution):

    def solve(self, inputs: Inputs) -> None:
        points, fold = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(points, fold))
        self.sample_results_2.append(self.solve_2(points, fold))

        points, fold = self.prepare(inputs.input)
        self.result_1 = self.solve_1(points, fold)
        self.result_2 = self.solve_2(points, fold)

    @staticmethod
    def prepare(data: str) -> tuple[set[Point2], list[Fold]]:
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

    @staticmethod
    def fold_once(points: set[Point2], fold: Fold) -> set[Point2]:
        new_points = set()
        for point in points:
            if point[fold.index] > fold.value:
                p = list(point)
                p[fold.index] = fold.value - (point[fold.index] - fold.value)
                point = Point2(*p)
            new_points.add(point)
        return new_points

    def solve_1(self, points: set[Point2], folds: list[Fold]) -> int:
        points = self.fold_once(points, folds[0])
        return len(points)

    def solve_2(self, points: set[Point2], folds: list[Fold]) -> str:
        for fold in folds:
            points = self.fold_once(points, fold)
        len_horizontal = max(points, key=lambda p: p.x).x + 1
        len_vertical = max(points, key=lambda p: p.y).y + 1
        code = [[" "] * len_horizontal for _ in range(len_vertical)]
        for point in points:
            code[point.y][point.x] = "█"
        return "\n".join("".join(line) for line in code)
