# https://adventofcode.com/2020/day/7

from typing import NamedTuple

from src.util.inputs import Inputs
from src.util.solution import Solution


NO_OTHER = "no other"
Bag = NamedTuple("Bag", (("n", int), ("type", str)))


class Solution2020Day07(Solution):

    def solve(self, inputs: Inputs) -> None:
        rules = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(rules))
        self.sample_results_2.append(self.solve_2(rules))
        rules = self.prepare(inputs.samples[1])
        self.sample_results_2.append(self.solve_2(rules))

        rules = self.prepare(inputs.input)
        self.result_1 = self.solve_1(rules)
        self.result_2 = self.solve_2(rules)

    @staticmethod
    def prepare(data: str) -> dict[str, list[Bag]]:
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

    def solve_1(self, rules: dict[str, list[Bag]]) -> int:
        return sum(self.search_shiny_gold(rules, bag) for bag in rules)

    def solve_2(self, rules: dict[str, list[Bag]]) -> int:
        return self.count_contents(rules, "shiny gold")

    def search_shiny_gold(self, rules: dict[str, list[Bag]], key: str) -> bool:
        for bag in rules[key]:
            if bag.type == "shiny gold" or bag.type != NO_OTHER and self.search_shiny_gold(rules, bag.type):
                return True
        return False

    def count_contents(self, rules: dict[str, list[Bag]], key: str) -> int:
        n = 0
        for bag in rules[key]:
            n += bag.n
            if bag.type != NO_OTHER:
                n += bag.n * self.count_contents(rules, bag.type)
        return n
