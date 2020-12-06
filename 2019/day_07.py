# https://adventofcode.com/2019/day/7


import itertools

from intcode import IntcodeComputer


def build_amps(code, feedback_mode=False, n=5):
    return [IntcodeComputer(code, True, feedback_mode) for _ in range(n)]


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


with open("day_07_input.txt") as file:
    program = [int(i) for i in file.read().split(",")]

# part 1:
test_code_1 = build_amps((3, 15, 3, 16, 1002, 16, 10, 16,
                          1, 16, 15, 15, 4, 15, 99, 0, 0))
assert test_phase_setting(test_code_1, (4, 3, 2, 1, 0)) == 43210
test_code_2 = build_amps((3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23,
                          101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0))
assert test_phase_setting(test_code_2, (0, 1, 2, 3, 4)) == 54321
test_code_3 = build_amps((3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31,
                          1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31,
                          1, 32, 31, 31, 4, 31, 99, 0, 0, 0))
assert test_phase_setting(test_code_3, (1, 0, 4, 3, 2)) == 65210
amplifiers = build_amps(program)
print(iterate_phases(amplifiers, range(5)))  # 21000

# part 2:
test_code_4 = build_amps((3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1,
                          27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99,
                          0, 0, 5), feedback_mode=True)
assert test_phase_setting(test_code_4, (9, 8, 7, 6, 5)) == 139629729
test_code_5 = build_amps((3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007,
                          54, 5, 55, 1005, 55, 26, 1001, 54, -5, 54, 1105, 1,
                          12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55,
                          2, 53, 55, 53, 4, 53, 1001, 56, -1, 56, 1005, 56, 6,
                          99, 0, 0, 0, 0, 10), feedback_mode=True)
assert test_phase_setting(test_code_5, (9, 7, 8, 5, 6)) == 18216
amplifiers = build_amps(program, feedback_mode=True)
print(iterate_phases(amplifiers, range(5, 10)))  # 61379886
