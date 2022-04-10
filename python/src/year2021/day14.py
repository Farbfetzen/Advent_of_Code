# https://adventofcode.com/2021/day/14

from collections import Counter
from functools import cache

from src.util.types import Data, Solution


def prepare_data(data: str) -> tuple[str, dict[str, str]]:
    template, _, *rules_list = data.splitlines()
    rules_dict = {k: v for k, v in (rule.split(" -> ") for rule in rules_list)}
    return template, rules_dict


def polymerize(template, rules, max_steps):
    @cache
    def count(pair, step):
        if step == max_steps or pair not in rules:
            return Counter()
        step += 1
        new_element = rules[pair]
        new_counter = Counter(new_element)
        new_counter.update(count(pair[0] + new_element, step))
        new_counter.update(count(new_element + pair[1], step))
        return new_counter

    counter = Counter(template)
    for left, right in zip(template, template[1:]):
        counter.update(count(left + right, 0))
    return counter


def get_difference(counter):
    sorted_by_frequency = counter.most_common()
    return sorted_by_frequency[0][1] - sorted_by_frequency[-1][1]


def part_1(template, rules):
    return get_difference(polymerize(template, rules, 10))


def part_2(template, rules):
    return get_difference(polymerize(template, rules, 40))


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_template, sample_rules = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_template, sample_rules))
    solution.samples_part_2.append(part_2(sample_template, sample_rules))

    challenge_template, challenge_rules = prepare_data(data.input)
    solution.part_1 = part_1(challenge_template, challenge_rules)
    solution.part_2 = part_2(challenge_template, challenge_rules)
    return solution
