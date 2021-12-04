# https://adventofcode.com/2019/day/14


from collections import defaultdict
from math import ceil


def get_ore_requirement(product, required_quantity):
    if product == "ORE":
        return required_quantity
    if excess[product] >= required_quantity:
        excess[product] -= required_quantity
        return 0
    required_quantity -= excess[product]
    excess[product] = 0
    product_quantity = reactions[product]["quantity"]
    reaction_repetitions = ceil(required_quantity / product_quantity)
    required_chemicals = reactions[product]["input"]
    ore = 0
    for chemical, quantity in required_chemicals.items():
        ore += get_ore_requirement(chemical, quantity * reaction_repetitions)
    excess[product] += product_quantity * reaction_repetitions - required_quantity
    return ore


reactions = {}
with open("../../input/2019-14-input.txt") as file:
    for line in file.read().splitlines():
        reaction = line.split(" => ")
        left = reaction[0].split(", ")[::-1]
        input_chemicals = {}
        while left:
            input_chemical = left.pop().split()
            input_chemicals[input_chemical[1]] = int(input_chemical[0])
        right = reaction[1].split()
        reactions[right[1]] = {
            "quantity": int(right[0]),
            "input": input_chemicals
        }

# part 1:
excess = defaultdict(int)
required_ore_for_1 = get_ore_requirement("FUEL", 1)
print(required_ore_for_1)  # 907302

# part 2:
available_ore = 1_000_000_000_000
excess = defaultdict(int)  # reset dictionary
fuel_to_produce = available_ore // required_ore_for_1
fuel_produced = 0
while available_ore > 0 and fuel_to_produce > 0:
    used_ore = get_ore_requirement("FUEL", fuel_to_produce)
    if used_ore > available_ore:
        fuel_to_produce //= 2
    else:
        fuel_produced += fuel_to_produce
        available_ore -= used_ore
print(fuel_produced)  # 1670299
