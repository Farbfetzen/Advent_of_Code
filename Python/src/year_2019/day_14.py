# https://adventofcode.com/2019/day/14

import collections
import math

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2019Day14(Solution):

    def solve(self, inputs: Inputs) -> None:
        for sample in inputs.samples:
            reactions = self.prepare(sample)
            required_ore_for_1 = self.get_ore_requirement(reactions, "FUEL", 1, collections.defaultdict(int))
            self.sample_results_1.append(required_ore_for_1)
            self.sample_results_2.append(self.solve_2(reactions, required_ore_for_1))

        reactions = self.prepare(inputs.input)
        required_ore_for_1 = self.get_ore_requirement(reactions, "FUEL", 1, collections.defaultdict(int))
        self.result_1 = required_ore_for_1
        self.result_2 = self.solve_2(reactions, required_ore_for_1)

    @staticmethod
    def prepare(data: str) -> dict[str, dict[str, int | dict[str, int]]]:
        reactions = {}
        for line in data.splitlines():
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
        return reactions

    def get_ore_requirement(
            self,
            reactions: dict[str, dict[str, int | dict[str, int]]],
            product: str,
            required_quantity: int,
            excess: collections.defaultdict[str, int]
    ) -> int:
        if product == "ORE":
            return required_quantity
        if excess[product] >= required_quantity:
            excess[product] -= required_quantity
            return 0
        required_quantity -= excess[product]
        excess[product] = 0
        product_quantity = reactions[product]["quantity"]
        reaction_repetitions = math.ceil(required_quantity / product_quantity)
        required_chemicals = reactions[product]["input"]
        ore = 0
        for chemical, quantity in required_chemicals.items():
            ore += self.get_ore_requirement(reactions, chemical, quantity * reaction_repetitions, excess)
        excess[product] += product_quantity * reaction_repetitions - required_quantity
        return ore

    def solve_2(
            self,
            reactions: dict[str, dict[str, int | dict[str, int]]],
            required_ore_for_1: int) -> int:
        available_ore = 1_000_000_000_000
        excess = collections.defaultdict(int)
        fuel_to_produce = available_ore // required_ore_for_1
        fuel_produced = 0
        while available_ore > 0 and fuel_to_produce > 0:
            used_ore = self.get_ore_requirement(reactions, "FUEL", fuel_to_produce, excess)
            if used_ore > available_ore:
                fuel_to_produce //= 2
            else:
                fuel_produced += fuel_to_produce
                available_ore -= used_ore
        return fuel_produced
