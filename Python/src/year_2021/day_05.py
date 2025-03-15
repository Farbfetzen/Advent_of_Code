# https://adventofcode.com/2021/day/5

import collections
import itertools
import re
from typing import Iterable, NamedTuple

from src.util.inputs import Inputs
from src.util.solution import Solution
from src.util.util import Point2


Line = NamedTuple("Line", (("start", Point2), ("end", Point2)))


class Solution2021Day05(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(prepared_input))
        self.sample_results_2.append(self.solve_2(prepared_input))

        prepared_input = self.prepare(inputs.input)
        self.result_1 = self.solve_1(prepared_input)
        self.result_2 = self.solve_2(prepared_input)

    @staticmethod
    def prepare(data: str) -> list[Line]:
        lines = data.splitlines()
        positions = ([int(x) for x in re.findall(r"\d+", line)] for line in lines)
        return [Line(Point2(*position[:2]), Point2(*position[2:])) for position in positions]

    @staticmethod
    def get_positions(line: Line) -> list[Point2]:
        positions = [line.start]
        slope_x = line.end.x - line.start.x
        slope_y = line.end.y - line.start.y
        dx = 0 if slope_x == 0 else slope_x // abs(slope_x)
        dy = 0 if slope_y == 0 else slope_y // abs(slope_y)
        pos = line.start
        while pos != line.end:
            pos = Point2(pos.x + dx, pos.y + dy)
            positions.append(pos)
        return positions

    def count_overlaps(self, lines: Iterable[Line]) -> int:
        positions = (self.get_positions(line) for line in lines)
        positions = itertools.chain.from_iterable(positions)
        counter = collections.Counter(positions)
        return sum(count > 1 for key, count in counter.items())

    def solve_1(self, lines: list[Line]) -> int:
        lines = (line for line in lines if line.start.x == line.end.x or line.start.y == line.end.y)
        return self.count_overlaps(lines)

    def solve_2(self, lines: list[Line]) -> int:
        return self.count_overlaps(lines)
