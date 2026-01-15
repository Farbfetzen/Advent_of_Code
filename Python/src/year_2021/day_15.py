# https://adventofcode.com/2021/day/15

import queue

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2021Day15(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(prepared_input))
        self.sample_results_2.append(self.solve_2(prepared_input))

        prepared_input = self.prepare(inputs.input)
        self.result_1 = self.solve_1(prepared_input)
        self.result_2 = self.solve_2(prepared_input)

    @staticmethod
    def prepare(data: str) -> list[list[int]]:
        return [[int(x) for x in line] for line in data.splitlines()]

    @staticmethod
    def manhattan_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def find_lowest_risk(self, cave_map: list[list[int]]) -> int:
        """Pathfinding using A*"""
        start = (0, 0)
        destination = (len(cave_map[0]) - 1, len(cave_map) - 1)
        frontier = queue.PriorityQueue()
        frontier.put((0, start))
        came_from = {start: None}
        risk_so_far = {start: 0}
        offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))
        pos = start
        while not frontier.empty():
            pos = frontier.get()[1]
            if pos == destination:
                break
            for offset in offsets:
                new_pos = (pos[0] + offset[0], pos[1] + offset[1])
                if 0 <= new_pos[0] < len(cave_map[0]) and 0 <= new_pos[1] < len(cave_map):
                    new_risk = risk_so_far[pos] + cave_map[new_pos[1]][new_pos[0]]
                    if new_pos not in came_from or new_risk < risk_so_far[new_pos]:
                        risk_so_far[new_pos] = new_risk
                        priority = new_risk + self.manhattan_distance(new_pos, destination)
                        frontier.put((priority, new_pos))
                        came_from[new_pos] = pos
        return risk_so_far[pos]

    def solve_1(self, cave_map: list[list[int]]) -> int:
        return self.find_lowest_risk(cave_map)

    def solve_2(self, cave_map: list[list[int]]) -> int:
        original_width = len(cave_map[0])
        original_height = len(cave_map)
        for i in range(4):
            for line in cave_map:
                right_part = [x % 9 + 1 for x in line[-original_width:]]
                line.extend(right_part)
            for line in cave_map[original_height * i : original_height * (i + 1)]:
                new_line = [x % 9 + 1 for x in line]
                cave_map.append(new_line)

        return self.find_lowest_risk(cave_map)
