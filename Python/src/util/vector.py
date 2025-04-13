import dataclasses
from typing import Self


@dataclasses.dataclass(frozen=True)
class Vector2:
    """Custom Vector2 class that only supports integers and is immutable as opposed to pygame.Vector2.
    Advent of code never deals with floats, so I wanted to write my own Vector2 just for fun.

    This class is immutable to make it safe for use in sets and as keys in dicts.

    Y increases downwards as is tradition for screen coordinates.
    This is useful because the puzzles I have come across assume this too.
    """

    x: int
    y: int

    def __post_init__(self) -> None:
        if not (isinstance(self.x, int) and isinstance(self.y, int)):
            raise TypeError(f"x and y must be integers, got x={type(self.x).__name__}, y={type(self.y).__name__}")

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other: Self) -> Self:
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __iadd__(self, other: Self) -> Self:
        return self.__add__(other)

    def __sub__(self, other: Self) -> Self:
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __isub__(self, other: Self) -> Self:
        return self.__sub__(other)

    def turn_right(self) -> Self:
        """Turn 90 degrees clockwise. Assumes that y increases downwards as usual for screen coordinates."""
        return Vector2(-self.y, self.x)

    def turn_left(self) -> Self:
        """Turn 90 degrees counterclockwise. Assumes that y increases downwards as usual for screen coordinates."""
        return Vector2(self.y, -self.x)
