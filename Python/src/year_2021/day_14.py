# https://adventofcode.com/2021/day/14

import collections
import functools

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2021Day14(Solution):

    def solve(self, inputs: Inputs) -> None:
        template, rules = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(template, rules))
        self.sample_results_2.append(self.solve_2(template, rules))

        template, rules = self.prepare(inputs.input)
        self.result_1 = self.solve_1(template, rules)
        self.result_2 = self.solve_2(template, rules)

    @staticmethod
    def prepare(data: str) -> tuple[str, dict[str, str]]:
        template, _, *rules_list = data.splitlines()
        rules_dict = {k: v for k, v in (rule.split(" -> ") for rule in rules_list)}
        return template, rules_dict

    @staticmethod
    def polymerize(template: str, rules: dict[str, str], max_steps: int) -> collections.Counter:
        @functools.cache
        def count(pair: str, step: int) -> collections.Counter:
            if step == max_steps or pair not in rules:
                return collections.Counter()
            step += 1
            new_element = rules[pair]
            new_counter = collections.Counter(new_element)
            new_counter.update(count(pair[0] + new_element, step))
            new_counter.update(count(new_element + pair[1], step))
            return new_counter

        counter = collections.Counter(template)
        for left, right in zip(template, template[1:]):
            counter.update(count(left + right, 0))
        return counter

    @staticmethod
    def get_difference(counter: collections.Counter) -> int:
        sorted_by_frequency = counter.most_common()
        return sorted_by_frequency[0][1] - sorted_by_frequency[-1][1]

    def solve_1(self, template: str, rules: dict[str, str]) -> int:
        return self.get_difference(self.polymerize(template, rules, 10))

    def solve_2(self, template: str, rules: dict[str, str]) -> int:
        return self.get_difference(self.polymerize(template, rules, 40))
