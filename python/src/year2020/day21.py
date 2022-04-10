# https://adventofcode.com/2020/day/21

from collections import defaultdict

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[str]:
    return data.splitlines()


def part_1(input_):
    allergen_ingredients = {}
    ingredient_counter = defaultdict(int)
    for line in input_:
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


def solve(data: Data) -> Solution:
    sample_data = prepare_data(data.samples[0])
    sample_sum_safe, sample_allergen_map = part_1(sample_data)

    challenge_data = prepare_data(data.input)
    challenge_sum_safe, challenge_allergen_map = part_1(challenge_data)

    return Solution(
        samples_part_1=[sample_sum_safe],
        samples_part_2=[part_2(sample_allergen_map)],
        part_1=challenge_sum_safe,
        part_2=part_2(challenge_allergen_map)
    )
