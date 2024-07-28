# https://adventofcode.com/2018/day/4

import re

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[str]:
    return sorted(data.splitlines())


def analyze_sleep_patterns(data: list[str]):
    sleep_patterns: dict[str, list[int]] = {}
    guard = ""
    sleep_start = -1
    pattern = re.compile(r".+:(\d\d)] ([a-zA-Z# ]+(\d+)?.+)")
    for line in data:
        groups = re.match(pattern, line).groups()  # type: ignore
        minute = int(groups[0])
        activity = groups[1]
        if activity == "falls asleep":
            sleep_start = minute
        elif activity == "wakes up":
            for m in range(sleep_start, minute):
                sleep_patterns[guard][m] += 1
        else:
            guard = groups[2]
            if guard not in sleep_patterns:
                sleep_patterns[guard] = [0] * 60
    return sleep_patterns


def part_1(data:  dict[str, list[int]]) -> int:
    sleepiest_guard = max(data, key=lambda k: sum(data[k]))
    minutes = data[sleepiest_guard]
    sleepiest_minute = minutes.index(max(minutes))
    return int(sleepiest_guard) * sleepiest_minute


def part_2(data: dict[str, list[int]]) -> int:
    best_guard = ""
    best_minute = -1
    num_asleep = -1
    for guard, minutes in data.items():
        n = max(minutes)
        if n > num_asleep:
            num_asleep = n
            best_guard = guard
            best_minute = minutes.index(n)
    return int(best_guard) * best_minute


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    sleep_patterns = analyze_sleep_patterns(sample_data)
    solution.samples_part_1.append(part_1(sleep_patterns))
    solution.samples_part_2.append(part_2(sleep_patterns))

    challenge_data = prepare_data(data.input)
    challenge_sleep_patterns = analyze_sleep_patterns(challenge_data)
    solution.part_1 = part_1(challenge_sleep_patterns)
    solution.part_2 = part_2(challenge_sleep_patterns)
    return solution
