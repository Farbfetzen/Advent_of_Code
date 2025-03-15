from typing import Type

from src.util.solution import Solution
from src.year_2022.day_01 import Solution2022Day01
from src.year_2022.day_02 import Solution2022Day02
from src.year_2022.day_03 import Solution2022Day03
from src.year_2022.day_04 import Solution2022Day04


solutions_2022: dict[int, Type[Solution]] = {
    1: Solution2022Day01,
    2: Solution2022Day02,
    3: Solution2022Day03,
    4: Solution2022Day04
}
