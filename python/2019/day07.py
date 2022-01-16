# https://adventofcode.com/2019/day/7


import itertools

from intcode import IntcodeComputer


INPUT_PATH = "../../input/2019-07-input.txt"
SAMPLE_PATH = "../../input/2019-07-sample.txt"


def get_data(filename):
    with open(filename) as file:
        return [[int(x) for x in line.split(",")] for line in file.read().splitlines()]


def build_amps(code, feedback_mode):
    return [IntcodeComputer(code, True, feedback_mode) for _ in range(5)]


def test_phase_setting(amps, phases):
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


def iterate_phases(amps, phase_range):
    max_signal = 0
    for phase_settings in itertools.permutations(phase_range):
        max_signal = max(
            test_phase_setting(amps, phase_settings),
            max_signal
        )
    return max_signal


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert test_phase_setting(build_amps(sample_data[0], False), (4, 3, 2, 1, 0)) == 43210
    assert test_phase_setting(build_amps(sample_data[1], False), (0, 1, 2, 3, 4)) == 54321
    assert test_phase_setting(build_amps(sample_data[2], False), (1, 0, 4, 3, 2)) == 65210
    assert test_phase_setting(build_amps(sample_data[3], True), (9, 8, 7, 6, 5)) == 139629729
    assert test_phase_setting(build_amps(sample_data[4], True), (9, 7, 8, 5, 6)) == 18216

    challenge_data = get_data(INPUT_PATH)[0]
    print(iterate_phases(build_amps(challenge_data, False), range(5)))  # 21000
    print(iterate_phases(build_amps(challenge_data, True), range(5, 10)))  # 61379886
