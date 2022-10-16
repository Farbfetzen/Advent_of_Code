# https://adventofcode.com/2019/day/12

# At first, I struggled with part 2, but then I found this comment on Reddit:
# https://www.reddit.com/r/adventofcode/comments/e9j0ve/2019_day_12_solutions/faja0lj
# The key insights are:
# 1) The axes (x,y,z) are totally independent. So it suffices to find the period
# for each axis separately. Then the answer is the least common multiple of these.
# 2) Each axis will repeat "relatively quickly" (fast enough to brute force)
# 3) Since each state has a unique parent, the first repeat must be a repeat of state 0.

import itertools
import math
import re

from src.util.types import Data, Solution


COMBINATIONS = list(itertools.combinations(range(4), 2))


def prepare_data(data: str) -> list[list[int]]:
    pattern = re.compile(r"-?\d+")
    return [[int(n) for n in re.findall(pattern, line)] for line in data.splitlines()]


def simulate(data: list[list[int]], n_steps: int) -> tuple[int, int]:
    x_positions = [d[0] for d in data]
    y_positions = [d[1] for d in data]
    z_positions = [d[2] for d in data]
    x_velocities = [0] * 4
    y_velocities = [0] * 4
    z_velocities = [0] * 4

    x_positions_original = x_positions.copy()
    y_positions_original = y_positions.copy()
    z_positions_original = z_positions.copy()
    x_velocities_original = x_velocities.copy()
    y_velocities_original = y_velocities.copy()
    z_velocities_original = z_velocities.copy()

    total_energy = 0
    x_period = 0
    y_period = 0
    z_period = 0

    i = 0
    while i < n_steps or x_period == 0 or y_period == 0 or z_period == 0:
        i += 1

        if x_period == 0 or i <= n_steps:
            apply_gravity(x_positions, x_velocities)
            if x_positions == x_positions_original and x_velocities == x_velocities_original:
                x_period = i
        if y_period == 0 or i <= n_steps:
            apply_gravity(y_positions, y_velocities)
            if y_positions == y_positions_original and y_velocities == y_velocities_original:
                y_period = i
        if z_period == 0 or i <= n_steps:
            apply_gravity(z_positions, z_velocities)
            if z_positions == z_positions_original and z_velocities == z_velocities_original:
                z_period = i

        if i == n_steps:
            for j in range(4):
                potential = sum(abs(n) for n in (x_positions[j], y_positions[j], z_positions[j]))
                kinetic = sum(abs(n) for n in (x_velocities[j], y_velocities[j], z_velocities[j]))
                total_energy += potential * kinetic

    return total_energy, math.lcm(x_period, y_period, z_period)


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


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data_0 = prepare_data(data.samples[0])
    sample_data_1 = prepare_data(data.samples[1])
    sample_solutions_0 = simulate(sample_data_0, 10)
    sample_solutions_1 = simulate(sample_data_1, 100)
    solution.samples_part_1.append(sample_solutions_0[0])
    solution.samples_part_1.append(sample_solutions_1[0])
    solution.samples_part_2.append(sample_solutions_0[1])
    solution.samples_part_2.append(sample_solutions_1[1])

    challenge_data = prepare_data(data.input)
    energy, period = simulate(challenge_data, 1000)
    solution.part_1 = energy
    solution.part_2 = period
    return solution
