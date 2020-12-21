# https://adventofcode.com/2020/day/19


from pprint import pprint
import itertools


def parse_input(input_txt):
    raw_rules, messages = (x.splitlines() for x in input_txt.split("\n\n"))
    rules = {}
    for rule in raw_rules:
        i, v = rule.split(":")
        i = int(i)
        v = v.strip().replace("\"", "").split("|")
        if len(v) == 1 and v[0] in "ab":
            rules[i] = v[0]
        else:
            rules[i] = [[int(x) for x in v.split()] for v in v]
    return rules, messages


def resolve_rules(rules, cache, i=0):
    if i in cache:
        return cache[i]
    rule = rules[i]
    if isinstance(rule, str):
        cache[i] = rule
        return rule
    out = []
    for option in rule:
        temp = [resolve_rules(rules, cache, next_i) for next_i in option]
        out.extend("".join(x) for x in itertools.product(*temp))
    cache[i] = out
    return out


def part_1(rules, messages):
    valid_messages = set(resolve_rules(rules, {}))
    return sum(message in valid_messages for message in messages)


def part_2(rules, messages):
    # 8: 42 | 42 8
    rules[8] = [[42], [42, 8]]
    # 11: 42 31 | 42 11 31
    rules[11] = [[42, 31], [42, 11, 31]]
    pprint(rules)

    # Do I get this right?
    # 8 returns these:
    # (42), (42, 42), (42, 42, 42), ...
    # and 11 returns these:
    # (42, 31), (42, 42, 31, 31), (42, 42, 42, 31, 31, 31), ...

    # Could I just check if a rule points to itself (i in option) and
    # then limit the recursion depth depending on the length of
    # the longest message? I don't think that would work because then "a"
    # or "b" would never be reached.

    # The loopy part comes in the second half of the rule. That means
    # [42] or [42, 31] are already resolved when it is reached.

    # Observation: In the test rules and challenge rules 0 points directly
    # to 8 and 11 in this order. And only 8 and 11 point to 42 and 31.

    return 0


test_input_1 = """\
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""
assert part_1(*parse_input(test_input_1)) == 2

test_input_2 = """\
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
"""
test_input_2 = parse_input(test_input_2)
assert part_1(*test_input_2) == 3
assert part_2(*test_input_2) == 12


with open("day_19_input.txt") as file:
    challenge_input = parse_input(file.read())
print(part_1(*challenge_input))  # 248
# print(part_2(challenge_input))  #
