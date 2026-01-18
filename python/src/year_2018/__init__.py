from typing import Type

from src.util.solution import Solution
from src.year_2018.day_01 import Solution2018Day01
from src.year_2018.day_02 import Solution2018Day02
from src.year_2018.day_03 import Solution2018Day03
from src.year_2018.day_04 import Solution2018Day04


solutions_2018: dict[int, Type[Solution]] = {
    1: Solution2018Day01,
    2: Solution2018Day02,
    3: Solution2018Day03,
    4: Solution2018Day04,
}
