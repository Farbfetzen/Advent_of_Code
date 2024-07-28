# https://adventofcode.com/2019/day/7

import itertools

from src.util.types import Data, Solution
from src.year2019.intcode import IntcodeComputer


def prepare_data(data: str) -> list[int]:
    return [int(x) for x in data.split(",")]


def build_amps(code: list[int], feedback_mode: bool) -> list[IntcodeComputer]:
    return [IntcodeComputer(code, True, feedback_mode) for _ in range(5)]


def test_phase_setting(amps: list[IntcodeComputer], phases: tuple[int, ...]) -> int:
    assert len(amps) == len(phases)
    signal = 0
    for amp, phase in zip(amps, phases):
        amp.reset()
        signal = amp.run([phase, signal])
    while not amps[0].has_halted:
        for amp in amps:
            new_signal = amp.run([signal])
            if new_signal is None:
                break
            signal = new_signal
    return signal


def iterate_phases(amps: list[IntcodeComputer], phase_range: range) -> int:
    max_signal = 0
    for phase_settings in itertools.permutations(phase_range):
        max_signal = max(
            test_phase_setting(amps, phase_settings),
            max_signal
        )
    return max_signal


def part_1(data: list[int]) -> int:
    return iterate_phases(build_amps(data, False), range(5))


def part_2(data: list[int]) -> int:
    return iterate_phases(build_amps(data, True), range(5, 10))


def solve(data: Data) -> Solution:
    solution = Solution()
    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
