# https://adventofcode.com/2018/day/3

import collections
import re

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2018Day03(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = inputs.samples[0].splitlines()
        sample_result_1, sample_result_2 = self.solve_both(prepared_input)
        self.sample_results_1.append(sample_result_1)
        self.sample_results_2.append(sample_result_2)

        prepared_input = inputs.input.splitlines()
        self.result_1, self.result_2 = self.solve_both(prepared_input)

    @staticmethod
    def get_claims(lines: list[str]) -> list[list[int]]:
        claims = []
        pattern = re.compile(r"(\d+)")
        for line in lines:
            claim = []
            for s in pattern.split(line):
                if s.isdigit():
                    claim.append(int(s))
            claims.append(claim)
        return claims

    def solve_both(self, data: list[str]) -> tuple[int, int]:
        all_coordinates = {}
        all_coordinates_list = []
        id_ = None
        for claim in self.get_claims(data):
            id_, left, top, width, height = claim
            claim_xy = []
            for x in range(left + 1, left + width + 1):
                for y in range(top + 1, top + height + 1):
                    claim_xy.append(str(x) + " " + str(y))
            all_coordinates[id_] = claim_xy
            all_coordinates_list += claim_xy

        counter_1 = collections.Counter(all_coordinates_list)
        counter_2 = collections.Counter(counter_1.values())
        if 1 in counter_2:
            del counter_2[1]

        unique = {k for k, v in counter_1.items() if v == 1}
        for id_, claim in all_coordinates.items():
            if set(claim).issubset(unique):
                break
        return sum(counter_2.values()), id_
