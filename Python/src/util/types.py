from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, NamedTuple


@dataclass
class Inputs:
    input: str = ""
    samples: list[str] = field(default_factory=lambda: [])


class Solution(ABC):

    def __init__(self):
        self.samples_1: list[int | str] = []
        self.samples_2: list[int | str] = []
        self.samples_other: dict[str, Any] = {}
        self.result_1: int | str = ""
        self.result_2: int | str = ""

    @abstractmethod
    def solve(self, inputs: Inputs) -> None:
        pass

    def __str__(self) -> str:
        samples_1 = self.format_result("samples part 1", self.samples_1)
        samples_2 = self.format_result("samples part 2", self.samples_2)
        samples_other = "\n\n".join(self.format_result(k, v) for k, v in self.samples_other.items())
        part_1 = self.format_result("part 1", self.result_1)
        part_2 = self.format_result("part 2", self.result_2)
        return "\n\n".join(s for s in (samples_1, samples_2, samples_other, part_1, part_2) if s)

    @staticmethod
    def format_result(heading: str, results: int | str | list) -> str | None:
        if results or results == 0:
            if isinstance(results, list):
                return heading + ":\n" + ", ".join(map(str, results))
            return heading + ":\n" + str(results)


Point2 = NamedTuple("Point2", (("x", int), ("y", int)))
