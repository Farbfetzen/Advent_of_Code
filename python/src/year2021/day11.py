# https://adventofcode.com/2021/day/11

from itertools import product

from src.util.types import Data, Solution


OFFSETS = list(product((-1, 0, 1), repeat=2))
OFFSETS.remove((0, 0))


def prepare_data(data: str) -> list[list[int]]:
    return [[int(x) for x in list(line)] for line in data.splitlines()]


class Octopuses:

    def __init__(self, energy_levels):
        self.energy_levels = energy_levels
        self.flashes_after_100_steps = 0
        self.steps = 0
        self.iterate()

    def increase_energy(self):
        for x, y in product(range(10), repeat=2):
            self.energy_levels[y][x] += 1

    def affect_neighbors(self, x, y):
        for dx, dy in OFFSETS:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 10 and 0 <= ny < 10 and self.energy_levels[ny][nx] > 0:
                self.energy_levels[ny][nx] += 1

    def step(self):
        finished = False
        flashes_in_this_step = 0
        while not finished:
            finished = True
            for x, y in product(range(10), repeat=2):
                if self.energy_levels[y][x] > 9:
                    finished = False
                    self.energy_levels[y][x] = 0
                    self.affect_neighbors(x, y)
                    flashes_in_this_step += 1
        return flashes_in_this_step

    def iterate(self):
        flashes = 0
        while flashes != 100:
            self.steps += 1
            self.increase_energy()
            flashes = self.step()
            if self.steps <= 100:
                self.flashes_after_100_steps += flashes


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    octopuses_sample = Octopuses(sample_data)
    solution.samples_part_1.append(octopuses_sample.flashes_after_100_steps)
    solution.samples_part_2.append(octopuses_sample.steps)

    challenge_data = prepare_data(data.input)
    octopuses_challenge = Octopuses(challenge_data)
    solution.part_1 = octopuses_challenge.flashes_after_100_steps
    solution.part_2 = octopuses_challenge.steps
    return solution
