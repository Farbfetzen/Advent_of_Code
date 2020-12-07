# https://adventofcode.com/2020/day/7


from collections import namedtuple


Bag = namedtuple("bag", ("n", "type"))


def parse_rules(rules):
    rules_dict = {}
    excluded = ("bags", "bag", "contain")
    for rule in rules:
        for punctuation in (",", "."):
            rule = rule.replace(punctuation, "")
        rule = [word for word in rule.split() if word not in excluded]
        key = " ".join(rule[:2])
        contents = rule[2:]
        if contents == ["no", "other"]:
            values = [Bag(0, "no other")]
        else:
            numbers = [int(word) for word in contents if word.isnumeric()]
            bag_types = [" ".join((adj, col))
                         for adj, col in zip(contents[1::3], contents[2::3])]
            values = [Bag(n, bt) for n, bt in zip(numbers, bag_types)]
        rules_dict[key] = values
    return rules_dict


def search_shiny_gold(rules, key):
    for bag in rules[key]:
        if bag.type == "shiny gold":
            return True
        elif bag.type != "no other" and search_shiny_gold(rules, bag.type):
            return True
    return False


def part_1(rules):
    return sum(search_shiny_gold(rules, bag) for bag in rules)


def count_contents(rules, key):
    n = 0
    for bag in rules[key]:
        n += bag.n
        if bag.type != "no other":
            n += bag.n * count_contents(rules, bag.type)
    return n


def part_2(rules):
    return count_contents(rules, "shiny gold")


test_rules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".splitlines()
test_rules_dict = parse_rules(test_rules)
assert part_1(test_rules_dict) == 4
assert part_2(test_rules_dict) == 32

test_rules_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.""".splitlines()
test_rules_2_dict = parse_rules(test_rules_2)
assert part_2(test_rules_2_dict) == 126


with open("day_07_input.txt") as file:
    bag_rules = parse_rules(file.read().splitlines())

print(part_1(bag_rules))  # 348
print(part_2(bag_rules))  # 18885
