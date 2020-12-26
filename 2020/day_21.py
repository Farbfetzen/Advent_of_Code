# https://adventofcode.com/2020/day/21


import collections


def part_1(input_txt):
    allergen_ingredients = {}
    ingredient_counter = collections.defaultdict(int)
    for line in input_txt.splitlines():
        i = line.index("(")
        ingredients = set(line[:i-1].split())
        allergens = line[i+10:-1].split(", ")
        for allergen in allergens:
            if allergen in allergen_ingredients:
                allergen_ingredients[allergen].intersection_update(ingredients)
            else:
                allergen_ingredients[allergen] = ingredients.copy()
        for ingredient in ingredients:
            ingredient_counter[ingredient] += 1

    without_allergens = set(ingredient_counter.keys())
    for v in allergen_ingredients.values():
        for allergen in v:
            without_allergens.discard(allergen)

    allergen_candidates = set()
    for v in allergen_ingredients.values():
        allergen_candidates.update(v)

    sum_ = sum(ingredient_counter[ingredient] for ingredient in without_allergens)
    return sum_, allergen_ingredients


def part_2(allergen_ingredients):
    finished = False
    done = set()
    while not finished:
        finished = True
        for allergen, ingredients in allergen_ingredients.items():
            if len(ingredients) == 1:
                # Get only element of set without removing it.
                ingredient = next(iter(ingredients))
                if ingredient not in done:
                    done.add(ingredient)
                    for a, i in allergen_ingredients.items():
                        if a != allergen:
                            i.discard(ingredient)
            else:
                finished = False
    result = [(k, *v) for k, v in allergen_ingredients.items()]
    result.sort(key=lambda x: x[0])
    return ",".join(x[1] for x in result)


test_input = """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""
sum_safe, allergen_map = part_1(test_input)
assert sum_safe == 5
assert part_2(allergen_map) == "mxmxvkd,sqjhc,fvjkl"

with open("day_21_input.txt") as file:
    challenge_input = file.read()
sum_safe, allergen_map = part_1(challenge_input)
print(sum_safe)  # 2061 is too high!
print(part_2(allergen_map))  # cdqvp,dglm,zhqjs,rbpg,xvtrfz,tgmzqjz,mfqgx,rffqhl
