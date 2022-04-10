# https://adventofcode.com/2020/day/7

from typing import NamedTuple

from src.util.types import Data, Solution


NO_OTHER = "no other"
Bag = NamedTuple("Bag", (("n", int), ("type", str)))


def prepare_data(data: str) -> dict[str, list[Bag]]:
    rules_dict = {}
    excluded = ("bags", "bag", "contain")
    for rule in data.splitlines():
        for punctuation in ",.":
            rule = rule.replace(punctuation, "")
        rule_list = [word for word in rule.split() if word not in excluded]
        key = " ".join(rule_list[:2])
        contents = rule_list[2:]
        if contents == ["no", "other"]:
            values = [Bag(0, NO_OTHER)]
        else:
            numbers = [int(word) for word in contents if word.isnumeric()]
            bag_types = [" ".join((adj, col)) for adj, col in zip(contents[1::3], contents[2::3])]
            values = [Bag(n, bt) for n, bt in zip(numbers, bag_types)]
        rules_dict[key] = values
    return rules_dict


def search_shiny_gold(rules, key):
    for bag in rules[key]:
        if (bag.type == "shiny gold" or
                bag.type != NO_OTHER and search_shiny_gold(rules, bag.type)):
            return True
    return False


def part_1(rules):
    return sum(search_shiny_gold(rules, bag) for bag in rules)


def count_contents(rules, key):
    n = 0
    for bag in rules[key]:
        n += bag.n
        if bag.type != NO_OTHER:
            n += bag.n * count_contents(rules, bag.type)
    return n


def part_2(rules):
    return count_contents(rules, "shiny gold")


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data_0 = prepare_data(data.samples[0])
    sample_data_1 = prepare_data(data.samples[1])
    solution.samples_part_1.append(part_1(sample_data_0))
    solution.samples_part_2.append(part_2(sample_data_0))
    solution.samples_part_2.append(part_2(sample_data_1))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
