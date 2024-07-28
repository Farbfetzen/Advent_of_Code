from dataclasses import dataclass, field
from typing import Any, NamedTuple, Protocol


@dataclass
class Data:

    input: str = ""
    samples: list[str] = field(default_factory=lambda: [])


@dataclass
class Solution:

    samples_part_1: list[int | str] = field(default_factory=lambda: [])
    samples_part_2: list[int | str] = field(default_factory=lambda: [])
    samples_other: dict[str, Any] = field(default_factory=lambda: {})
    part_1: int | str = ""
    part_2: int | str = ""

    def __str__(self) -> str:
        samples_1 = self.format_solution("samples part 1", self.samples_part_1)
        samples_2 = self.format_solution("samples part 2", self.samples_part_2)
        samples_other = ""
        if self.samples_other:
            samples_other = "\n\n".join(self.format_solution(k, v) for k, v in self.samples_other.items())
        part_1 = self.format_solution("part 1", self.part_1)
        part_2 = self.format_solution("part 2", self.part_2)
        return "\n\n".join(s for s in (samples_1, samples_2, samples_other, part_1, part_2) if s)

    @staticmethod
    def format_solution(heading: str, values: int | str | list) -> str:
        if values:
            if isinstance(values, list):
                return heading + ":\n" + ", ".join(map(str, values))
            return heading + ":\n" + str(values)
        return ""


class ModuleWithSolveFunction(Protocol):
    """An interface for the day modules. All they need is
    a module-level function that conforms to this solve method.

    This allows for static type checking. Use it like this:
    module = importlib.import_module("foo.bar.baz")
    solution_module = typing.cast(ModuleWithSolveFunction, module)

    I got the idea from https://stackoverflow.com/a/49011396/16724834.
    """

    @staticmethod
    def solve(data: Data) -> Solution:
        ...


Point2 = NamedTuple("Point2", (("x", int), ("y", int)))
