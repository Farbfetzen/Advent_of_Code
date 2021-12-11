# https://adventofcode.com/2021/day/11


from itertools import product


SAMPLE_PATH = "../../input/2021-11-sample.txt"
INPUT_PATH = "../../input/2021-11-input.txt"
OFFSETS = list(product((-1, 0, 1), repeat=2))
OFFSETS.remove((0, 0))


class Octopuses:

    def __init__(self, filename):
        self.energy_levels = self.get_data(filename)
        self.flashes_after_100_steps = 0
        self.steps = 0
        self.iterate()

    @staticmethod
    def get_data(filename):
        with open(filename) as file:
            data = file.read().splitlines()
        return [[int(x) for x in list(line)] for line in data]

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


if __name__ == "__main__":
    octopuses_sample = Octopuses(SAMPLE_PATH)
    assert octopuses_sample.flashes_after_100_steps == 1656
    assert octopuses_sample.steps == 195

    octopuses_challenge = Octopuses(INPUT_PATH)
    print(octopuses_challenge.flashes_after_100_steps)  # 1721
    print(octopuses_challenge.steps)  # 298
