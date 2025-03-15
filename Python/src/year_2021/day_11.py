# https://adventofcode.com/2021/day/11

import itertools

from src.util.inputs import Inputs
from src.util.solution import Solution


OFFSETS = list(itertools.product((-1, 0, 1), repeat=2))
OFFSETS.remove((0, 0))


class Octopuses:

    def __init__(self, energy_levels) -> None:
        self.energy_levels = energy_levels
        self.flashes_after_100_steps = 0
        self.steps = 0
        self.iterate()

    def increase_energy(self) -> None:
        for x, y in itertools.product(range(10), repeat=2):
            self.energy_levels[y][x] += 1

    def affect_neighbors(self, x, y) -> None:
        for dx, dy in OFFSETS:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 10 and 0 <= ny < 10 and self.energy_levels[ny][nx] > 0:
                self.energy_levels[ny][nx] += 1

    def step(self) -> int:
        finished = False
        flashes_in_this_step = 0
        while not finished:
            finished = True
            for x, y in itertools.product(range(10), repeat=2):
                if self.energy_levels[y][x] > 9:
                    finished = False
                    self.energy_levels[y][x] = 0
                    self.affect_neighbors(x, y)
                    flashes_in_this_step += 1
        return flashes_in_this_step

    def iterate(self) -> None:
        flashes = 0
        while flashes != 100:
            self.steps += 1
            self.increase_energy()
            flashes = self.step()
            if self.steps <= 100:
                self.flashes_after_100_steps += flashes


class Solution2021Day11(Solution):

    def solve(self, inputs: Inputs) -> None:
        octopuses_sample = Octopuses(self.prepare(inputs.samples[0]))
        self.sample_results_1.append(octopuses_sample.flashes_after_100_steps)
        self.sample_results_2.append(octopuses_sample.steps)

        octopuses_puzzle = Octopuses(self.prepare(inputs.input))
        self.result_1 = octopuses_puzzle.flashes_after_100_steps
        self.result_2 = octopuses_puzzle.steps

    @staticmethod
    def prepare(data: str) -> list[list[int]]:
        return [[int(x) for x in list(line)] for line in data.splitlines()]
