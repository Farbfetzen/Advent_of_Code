# https://adventofcode.com/2020/day/7


from collections import namedtuple


Bag = namedtuple("bag", ("n", "type"))


def get_data(filename):
    with open(filename) as file:
        return file.read()


def parse_rules(rules):
    rules_dict = {}
    excluded = ("bags", "bag", "contain")
    for rule in rules.splitlines():
        for punctuation in ",.":
            rule = rule.replace(punctuation, "")
        rule = [word for word in rule.split() if word not in excluded]
        key = " ".join(rule[:2])
        contents = rule[2:]
        if contents == ["no", "other"]:
            values = [Bag(0, "no other")]
        else:
            numbers = [int(word) for word in contents if word.isnumeric()]
            bag_types = [" ".join((adj, col)) for adj, col in zip(contents[1::3], contents[2::3])]
            values = [Bag(n, bt) for n, bt in zip(numbers, bag_types)]
        rules_dict[key] = values
    return rules_dict


def search_shiny_gold(rules, key):
    for bag in rules[key]:
        if (bag.type == "shiny gold" or
                bag.type != "no other" and search_shiny_gold(rules, bag.type)):
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


sample_data = get_data("../../input/2020-07-sample.txt")
sample_data = [parse_rules(data) for data in sample_data.split("\n\n")]
challenge_data = parse_rules(get_data("../../input/2020-07-input.txt"))

if __name__ == "__main__":
    assert part_1(sample_data[0]) == 4
    assert part_2(sample_data[0]) == 32
    assert part_2(sample_data[1]) == 126

    print(part_1(challenge_data))  # 348
    print(part_2(challenge_data))  # 18885
