from abc import ABC, abstractmethod
from typing import Any

from src.util.inputs import Inputs


class Solution(ABC):

    def __init__(self) -> None:
        self.sample_results_1: list[int | str] = []
        self.sample_results_2: list[int | str] = []
        self.sample_results_other: dict[int | str, Any] = {}
        self.result_1: int | str = 0
        self.result_2: int | str = 0

    @abstractmethod
    def solve(self, inputs: Inputs) -> None:
        pass

    def __str__(self) -> str:
        samples_1 = self.format_result("samples part 1", self.sample_results_1)
        samples_2 = self.format_result("samples part 2", self.sample_results_2)
        samples_other = "\n\n".join(self.format_result(str(k), v) for k, v in self.sample_results_other.items())
        part_1 = self.format_result("part 1", self.result_1)
        part_2 = self.format_result("part 2", self.result_2)
        return "\n\n".join(s for s in (samples_1, samples_2, samples_other, part_1, part_2) if s)

    @staticmethod
    def format_result(heading: str, results: int | str | list) -> str | None:
        if results or results == 0:
            if isinstance(results, list):
                return heading + ":\n" + ", ".join(map(str, results))
            return heading + ":\n" + str(results)
