from typing import Type

from src import Solution
from src.year_2019.day_01 import Solution2019Day01
from src.year_2019.day_03 import Solution2019Day03
from src.year_2019.day_04 import Solution2019Day04
from src.year_2019.day_06 import Solution2019Day06
from src.year_2019.day_08 import Solution2019Day08
from src.year_2019.day_10 import Solution2019Day10
from src.year_2019.day_12 import Solution2019Day12
from src.year_2019.day_14 import Solution2019Day14
from src.year_2019.day_16 import Solution2019Day16
from src.year_2019.day_18 import Solution2019Day18
from src.year_2019.day_20 import Solution2019Day20
from src.year_2019.day_22 import Solution2019Day22


solutions_2019: dict[int, Type[Solution]] = {
    1: Solution2019Day01,
    3: Solution2019Day03,
    4: Solution2019Day04,
    6: Solution2019Day06,
    8: Solution2019Day08,
    10: Solution2019Day10,
    12: Solution2019Day12,
    14: Solution2019Day14,
    16: Solution2019Day16,
    18: Solution2019Day18,
    20: Solution2019Day20,
    22: Solution2019Day22,
}
