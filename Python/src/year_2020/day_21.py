# https://adventofcode.com/2020/day/21

import collections

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2020Day21(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = inputs.samples[0].splitlines()
        sum_safe, allergen_map = self.solve_1(prepared_input)
        self.sample_results_1.append(sum_safe)
        self.sample_results_2.append(self.solve_2(allergen_map))

        prepared_input = inputs.input.splitlines()
        sum_safe, allergen_map = self.solve_1(prepared_input)
        self.result_1 = sum_safe
        self.result_2 = self.solve_2(allergen_map)

    @staticmethod
    def solve_1(data: list[str]) -> tuple[int, dict[str, set[str]]]:
        allergen_ingredients = {}
        ingredient_counter = collections.defaultdict(int)
        for line in data:
            i = line.index("(")
            ingredients = set(line[:i - 1].split())
            allergens = line[i + 10:-1].split(", ")
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

    @staticmethod
    def solve_2(allergen_ingredients: dict[str, set[str]]) -> str:
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
