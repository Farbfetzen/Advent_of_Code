# https://adventofcode.com/2019/day/12

import itertools
import math
import re
from dataclasses import dataclass, field

from src.util.inputs import Inputs
from src.util.solution import Solution


COMBINATIONS = list(itertools.combinations(range(4), 2))


@dataclass
class SimulationData:
    period: int
    positions: list[int]
    velocities: list[int]

    original_positions: list[int] = field(init=False)
    original_velocities: list[int] = field(init=False)

    def __post_init__(self):
        self.original_positions = self.positions.copy()
        self.original_velocities = self.velocities.copy()


class Solution2019Day12(Solution):

    def solve(self, inputs: Inputs) -> None:
        for sample, n_steps in zip(inputs.samples, (10, 100)):
            energy, period = self.simulate(self.prepare(sample), n_steps)
            self.sample_results_1.append(energy)
            self.sample_results_2.append(period)

        self.result_1, self.result_2 = self.simulate(self.prepare(inputs.input), 1000)

    @staticmethod
    def prepare(data: str) -> list[list[int]]:
        pattern = re.compile(r"-?\d+")
        return [[int(n) for n in re.findall(pattern, line)] for line in data.splitlines()]

    @staticmethod
    def apply_gravity(positions: list[int], velocities: list[int]) -> None:
        for i, j in COMBINATIONS:
            if positions[i] > positions[j]:
                velocities[i] -= 1
                velocities[j] += 1
            elif positions[i] < positions[j]:
                velocities[i] += 1
                velocities[j] -= 1
        for i in range(4):
            positions[i] += velocities[i]

    @staticmethod
    def calculate_energy(i: int, n_steps: int, xyz: tuple[SimulationData, SimulationData, SimulationData]) -> int:
        energy = 0
        if i == n_steps:
            for j in range(4):
                potential = sum(abs(n) for n in (xyz[0].positions[j], xyz[1].positions[j], xyz[2].positions[j]))
                kinetic = sum(abs(n) for n in (xyz[0].velocities[j], xyz[1].velocities[j], xyz[2].velocities[j]))
                energy += potential * kinetic
        return energy

    def simulate(self, data: list[list[int]], n_steps: int) -> tuple[int, int]:
        total_energy = 0
        xyz = (
            SimulationData(0, [d[0] for d in data], [0] * 4),
            SimulationData(0, [d[1] for d in data], [0] * 4),
            SimulationData(0, [d[2] for d in data], [0] * 4)
        )

        i = 0
        while i < n_steps or any(dim.period == 0 for dim in xyz):
            i += 1
            for dim in xyz:
                if dim.period == 0:
                    self.apply_gravity(dim.positions, dim.velocities)
                    if dim.positions == dim.original_positions and dim.velocities == dim.original_velocities:
                        dim.period = i
            total_energy += self.calculate_energy(i, n_steps, xyz)
        return total_energy, math.lcm(xyz[0].period, xyz[1].period, xyz[2].period)
