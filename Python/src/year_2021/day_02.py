# https://adventofcode.com/2021/day/2

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2021Day02(Solution):

    def solve(self, inputs: Inputs) -> None:
        horizontal_position, depth, aim = self.follow_course(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(horizontal_position, aim))
        self.sample_results_2.append(self.solve_2(horizontal_position, depth))

        horizontal_position, depth, aim = self.follow_course(inputs.input)
        self.result_1 = self.solve_1(horizontal_position, aim)
        self.result_2 = self.solve_2(horizontal_position, depth)

    @staticmethod
    def follow_course(data: str) -> tuple[int, int, int]:
        """Both parts can be done in one pass because aim in part 2 is just depth from part 1."""
        course = [(direction, int(n)) for direction, n in (line.split() for line in data.splitlines())]
        horizontal_position = 0
        depth = 0
        aim = 0
        for direction, n in course:
            if direction == "forward":
                horizontal_position += n
                depth += aim * n
            elif direction == "up":
                aim -= n
            elif direction == "down":
                aim += n
        return horizontal_position, depth, aim

    @staticmethod
    def solve_1(horizontal_position: int, aim: int) -> int:
        return horizontal_position * aim

    @staticmethod
    def solve_2(horizontal_position: int, depth: int) -> int:
        return horizontal_position * depth
