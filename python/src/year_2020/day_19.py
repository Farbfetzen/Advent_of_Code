# https://adventofcode.com/2020/day/19

import itertools

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2020Day19(Solution):

    def solve(self, inputs: Inputs) -> None:
        rules, messages = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(rules, messages))
        rules, messages = self.prepare(inputs.samples[1])
        self.sample_results_1.append(self.solve_1(rules, messages))
        self.sample_results_2.append(self.solve_2(rules, messages))

        rules, messages = self.prepare(inputs.input)
        self.result_1 = self.solve_1(rules, messages)
        self.result_2 = self.solve_2(rules, messages)

    @staticmethod
    def prepare(data: str) -> tuple[dict[int, str | list[list[int]]], list[str]]:
        raw_rules, messages = (x.splitlines() for x in data.split("\n\n"))
        rules: dict[int, str | list[list[int]]] = {}
        for rule in raw_rules:
            i_str, v_str = rule.split(":")
            i = int(i_str)
            v = v_str.strip().replace('"', "").split("|")
            if len(v) == 1 and v[0] in "ab":
                rules[i] = v[0]
            else:
                rules[i] = [[int(x) for x in v.split()] for v in v]
        return rules, messages

    def resolve_rules(self, rules: dict[int, str | list[list[int]]], cache: dict, i=0):
        # Recursive search with memoization.
        if i in cache:
            return cache[i]
        rule = rules[i]
        if isinstance(rule, str):
            cache[i] = rule
            return rule
        out = []
        # I call "option" the part of a rule that is delimited by a "|".
        # Most rules have two options.
        for option in rule:
            temp = [self.resolve_rules(rules, cache, next_i) for next_i in option]
            out.extend("".join(x) for x in itertools.product(*temp))
        cache[i] = out
        return out

    def solve_1(self, rules: dict[int, str | list[list[int]]], messages: list[str]) -> int:
        valid_messages = set(self.resolve_rules(rules, {}))
        return sum(message in valid_messages for message in messages)

    def solve_2(self, rules: dict[int, str | list[list[int]]], messages: list[str]) -> int:
        # For an explanation see the bottom of this script.

        # 8: 42 | 42 8
        rules[8] = [[42], [42, 8]]
        # 11: 42 31 | 42 11 31
        rules[11] = [[42, 31], [42, 11, 31]]

        rule_cache = {}  # share the cache for both searches
        r_31 = set(self.resolve_rules(rules, rule_cache, 31))
        r_42 = set(self.resolve_rules(rules, rule_cache, 42))
        len_31 = {len(x) for x in r_31}
        len_42 = {len(x) for x in r_42}
        len_both = len_31 | len_42
        assert len(len_both) == 1
        word_len = len_both.pop()

        sum_valid = 0
        for m in messages:
            words = [m[0 + i : word_len + i] for i in range(0, len(m), word_len)]
            n_words = len(words)

            n_31 = 0
            for word in reversed(words):
                if word in r_31:
                    n_31 += 1
                else:
                    break
            if 0 < n_31 < n_words / 2 and all(word in r_42 for word in words[:-n_31]):
                sum_valid += 1

        return sum_valid


# Explanation for part 2:
#
# - Rule 8 returns these:
#   (42), (42, 42), (42, 42, 42), ...
#   And rule 11 returns these:
#   (42, 31), (42, 42, 31, 31), (42, 42, 42, 31, 31, 31), ...
#
# - The loopy part comes in the second half of the rules. That means
#   [42] or [42, 31] are already resolved when it is reached.
#
# - In the test rules and challenge rules, rule 0 points directly
#   to 8 and 11 IN THIS ORDER. That means every valid rule must follow
#   one of these patterns:
#   1. left + left:   42, 42, 31
#   2. left + right:  42, 42 * x, 31 * x
#   3. right + left:  42 * x, 42, 31
#   4. right + right: 42 * x, 42 * y, 31 * y
#   They have in common that the left part is all 42, the right part
#   is all 31 and the number of 31 is less than the number of 42.
#
# - Remember: Solve the challenge for the rules given, not any
#   general rules! Start by resolving only rules 31 and 42.
#   Then check the patterns.
#
# - Complication: 42 and 31 have many possibilities. But both are always
#   the same length. I can split each message into n-character words.
