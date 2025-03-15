# https://adventofcode.com/2019/day/6

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2019Day06(Solution):

    def solve(self, inputs: Inputs) -> None:
        orbits = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(orbits))
        orbits = self.prepare(inputs.samples[1])
        self.sample_results_2.append(self.solve_2(orbits))

        orbits = self.prepare(inputs.input)
        self.result_1 = self.solve_1(orbits)
        self.result_2 = self.solve_2(orbits)

    @staticmethod
    def prepare(data: str) -> dict[str, str]:
        orbits = {}
        for line in data.splitlines():
            a, b = line.split(")")
            orbits[b] = a
        return orbits

    @staticmethod
    def find_com(orbits: dict[str, str], start: str) -> list[str]:
        path = []
        position = orbits[start]
        while position != "COM":
            path.append(position)
            position = orbits[position]
        return path

    def solve_1(self, orbits: dict[str, str]) -> int:
        total = 0
        for o in orbits:
            total += len(self.find_com(orbits, o)) + 1
        return total

    def solve_2(self, orbits: dict[str, str]) -> int:
        you_to_com = self.find_com(orbits, "YOU")
        san_to_com = self.find_com(orbits, "SAN")
        jumps = set(you_to_com).symmetric_difference(san_to_com)
        return len(jumps)
