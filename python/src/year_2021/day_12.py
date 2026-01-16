# https://adventofcode.com/2021/day/12

import collections
import functools

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2021Day12(Solution):

    def solve(self, inputs: Inputs) -> None:
        for sample in inputs.samples:
            prepared_input = self.prepare(sample)
            self.sample_results_1.append(self.solve_1(prepared_input))
            self.sample_results_2.append(self.solve_2(prepared_input))

        prepared_input = self.prepare(inputs.input)
        self.result_1 = self.solve_1(prepared_input)
        self.result_2 = self.solve_2(prepared_input)

    @staticmethod
    def prepare(data: str) -> collections.defaultdict[str, list]:
        cave_map = collections.defaultdict(list)
        for line in data.splitlines():
            a, b = line.split("-")
            cave_map[a].append(b)
            cave_map[b].append(a)
        return cave_map

    @staticmethod
    def count_paths(cave_map: collections.defaultdict[str, list], single_small_twice: bool) -> int:
        # Use functools.cache to eliminate unnecessary recursive calls.
        @functools.cache
        def count_next_paths(origin: str, seen: frozenset[str], twice: bool) -> int:
            if origin.islower():
                seen = seen.union({origin})
            n_paths = 0
            for target in cave_map[origin]:
                if target == "end":
                    n_paths += 1
                elif target not in seen:
                    n_paths += count_next_paths(target, seen, twice)
                elif target != "start" and twice:
                    n_paths += count_next_paths(target, seen, False)
            return n_paths

        return count_next_paths("start", frozenset(), single_small_twice)

    def solve_1(self, cave_map: collections.defaultdict[str, list]) -> int:
        return self.count_paths(cave_map, False)

    def solve_2(self, cave_map: collections.defaultdict[str, list]) -> int:
        return self.count_paths(cave_map, True)
