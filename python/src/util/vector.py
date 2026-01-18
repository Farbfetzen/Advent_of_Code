from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True, slots=True, order=True)
class Vector2:
    """Custom Vector2 class that only supports integers and is immutable as opposed to pygame.Vector2.
    Advent of code never deals with floats, so I wanted to write my own Vector2 just for fun.

    This class is immutable to make it safe for use in sets and as keys in dicts.

    Y increases downwards as is tradition for screen coordinates.
    This is useful because the puzzles I have come across assume this too.
    """

    x: int
    y: int

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Keeping the string short to make debugging easier because usually there are many Vectors in a collection."""
        return f"V2({self.x}, {self.y})"

    def __add__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: "Vector2") -> "Vector2":
        return self.__add__(other)

    def __sub__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x - other.x, self.y - other.y)

    def __isub__(self, other: "Vector2") -> "Vector2":
        return self.__sub__(other)

    def __iter__(self) -> Iterator[int]:
        return iter((self.x, self.y))

    def turn_right(self) -> "Vector2":
        """Turn 90 degrees clockwise. Assumes that y increases downwards as usual for screen coordinates."""
        return Vector2(-self.y, self.x)

    def turn_left(self) -> "Vector2":
        """Turn 90 degrees counterclockwise. Assumes that y increases downwards as usual for screen coordinates."""
        return Vector2(self.y, -self.x)

    def above(self) -> "Vector2":
        """Returns the position above, reducing y by 1."""
        return Vector2(self.x, self.y - 1)

    def below(self) -> "Vector2":
        """Returns the position below, increasing y by 1."""
        return Vector2(self.x, self.y + 1)

    def left(self) -> "Vector2":
        return Vector2(self.x - 1, self.y)

    def right(self) -> "Vector2":
        return Vector2(self.x + 1, self.y)

    def neighbors_4(self) -> tuple["Vector2", "Vector2", "Vector2", "Vector2"]:
        """Returns the 4 horizontal and vertical neighbors clockwise, starting from the top."""
        return self.above(), self.right(), self.below(), self.left()

    def manhattan_distance(self, other: "Vector2") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)
