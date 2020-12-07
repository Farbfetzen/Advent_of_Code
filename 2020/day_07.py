# https://adventofcode.com/2020/day/7


from pprint import pprint


# def parse_rules(rules):
#     rule_dict = {}
#     exclude = ("bags", "bag", "contain", ",", ".")
#     all_bags = set()
#     for rule in rules:
#         for exc in exclude:
#             rule = rule.replace(exc, "")
#         rule = rule.split()
#         rule = [r for r in rule if r.isalpha()]
#         rule = [adj + " " + col for adj, col in zip(rule[::2], rule[1::2])]
#         key = rule[0]
#         values = rule[1:]
#         rule_dict[key] = values
#         all_bags.update(rule)
#     # invert the dict so key bags can be contained in any of the value bags
#     inverted_rules = {k: [] for k in all_bags}
#     for k, v in rule_dict.items():
#         for bag in v:
#             inverted_rules[bag].append(k)
#     # pprint(inverted_rules)
#     return inverted_rules


def parse_rules(rules):
    rule_dict = {}
    excluded = ("bags", "bag", "contain")
    for rule in rules:
        rule = [word for word in rule.split()
                if word.isalpha() and word not in excluded]
        rule = [adj + " " + col for adj, col in zip(rule[::2], rule[1::2])]
        rule_dict[rule[0]] = rule[1:]
    return rule_dict


def search_shiny_gold(rules, key):
    # Recursively search for a shiny gold bag and return True if found.
    for bag in rules[key]:
        if (bag == "shiny gold"
                or bag != "no other" and search_shiny_gold(rules, bag)):
            return True
    return False


def part_1(rules):
    return sum(search_shiny_gold(rules, bag) for bag in rules)


test_rules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".splitlines()
test_rule_dict = parse_rules(test_rules)

assert part_1(test_rule_dict) == 4


with open("day_07_input.txt") as file:
    rules = parse_rules(file.read().splitlines())

print(part_1(rules))  # 348
