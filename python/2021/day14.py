# https://adventofcode.com/2021/day/14


from collections import Counter
from functools import cache


SAMPLE_PATH = "../../input/2021-14-sample.txt"
INPUT_PATH = "../../input/2021-14-input.txt"


def get_data(filename):
    with open(filename) as file:
        template, _, *rules = file.read().splitlines()
    rules = {k: v for k, v in (rule.split(" -> ") for rule in rules)}
    return template, rules


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


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(*sample_data) == 1588
    assert part_2(*sample_data) == 2188189693529

    challenge_data = get_data(INPUT_PATH)
    print(part_1(*challenge_data))  # 2768
    print(part_2(*challenge_data))  # 2914365137499
