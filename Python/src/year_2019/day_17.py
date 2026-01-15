# https://adventofcode.com/2019/day/17

from src.util.exceptions import ResultExpectedError
from src.util.inputs import Inputs
from src.util.solution import Solution
from src.util.vector import Vector2
from src.year_2019.intcode import IntcodeComputer


type Functions = dict[str, tuple[str, ...]]
type MainRoutine = tuple[str, ...]


class Solution2019Day17(Solution):

    def __init__(self) -> None:
        super().__init__()
        self.scaffolds: set[Vector2] = set()
        self.start_position = Vector2(-1, -1)
        self.start_direction = Vector2(-1, -1)
        self.intersections: set[Vector2] = set()
        self.path: list[str] = []

    def solve(self, inputs: Inputs) -> None:
        self.analyze_scaffold(inputs.input)
        self.construct_paths()
        self.solve_1()
        self.solve_2(inputs.input)

    def analyze_scaffold(self, program: str) -> None:
        scaffold_view = IntcodeComputer(program).run_ascii()[0]
        # Visual inspection of the scaffold reveals that it's a single line with one start, one end and no tangents.
        # See the bottom of this script.
        # print(scaffold_view)

        for y, line in enumerate(scaffold_view.split("\n")):
            for x, char in enumerate(line):
                if char == "#":
                    self.scaffolds.add(Vector2(x, y))
                elif char != ".":
                    self.start_position = Vector2(x, y)
                    if char == ">":
                        self.start_direction = Vector2(1, 0)
                    elif char == "<":
                        self.start_direction = Vector2(-1, 0)
                    elif char == "^":
                        self.start_direction = Vector2(0, -1)
                    else:
                        self.start_direction = Vector2(0, 1)
        assert self.start_direction != Vector2(-1, -1)
        assert self.start_position != Vector2(-1, -1)

    def construct_paths(self) -> None:
        """Walk the scaffolds and record the paths taken.
        I know that the part 2 is solvable if I record just the simplest path.
        If that weren't the case I would have to split the possible paths at the intersections
        and try those alternatives in part 2.
        """
        position = self.start_position
        direction = self.start_direction
        steps_in_one_direction = 0
        visited_positions = {position}
        while True:
            if (new_position := position + direction) in self.scaffolds:
                steps_in_one_direction += 1
            else:
                self.path.append(str(steps_in_one_direction))
                steps_in_one_direction = 1
                left = direction.turn_left()
                right = direction.turn_right()
                if (new_position := position + left) in self.scaffolds:
                    direction = left
                    self.path.append("L")
                elif (new_position := position + right) in self.scaffolds:
                    direction = right
                    self.path.append("R")
                else:
                    break
            if new_position in visited_positions:
                self.intersections.add(new_position)
            visited_positions.add(new_position)
            position = new_position
        if self.path[0] == "0":
            del self.path[0]

    def solve_1(self) -> None:
        self.result_1 = sum(i.x * i.y for i in self.intersections)

    def solve_2(self, program: str) -> None:
        # Part 2 can be solved manually by simply looking at the path.
        # But here is an automated way to partition the path.
        result = self.partition_path(tuple(self.path), (), {})
        if result is None:
            raise ResultExpectedError("No valid path compression found.")
        main_routine, functions = result
        main_routine = ",".join(main_routine)
        a = ",".join(functions["A"])
        b = ",".join(functions["B"])
        c = ",".join(functions["C"])

        robot = IntcodeComputer(program)
        robot.memory[0] = 2
        _output = robot.run_ascii()[0]
        # print(_output)  # prints the map and then "Main:"
        _output = robot.run_ascii(main_routine)[0]
        # print(_output)  # prints "Function A:"
        _output = robot.run_ascii(a)[0]
        # print(_output)  # prints "Function B:"
        _output = robot.run_ascii(b)[0]
        # print(_output)  # prints "Function C:"
        _output = robot.run_ascii(c)[0]
        # print(_output)  # prints "Continuous video feed?"
        *_final_map_state, dust_amount = robot.run_ascii("n")
        # print("".join(_final_map_state))
        self.result_2 = dust_amount

    def partition_path(
        self, remaining_path: tuple[str, ...], main_routine: MainRoutine, functions: Functions
    ) -> tuple[MainRoutine, Functions] | None:
        # I'm using tuples instead of strings because an instruction like "L10"
        # must be parsed as ("L", "10"), not ("L", "1", "0").
        if not remaining_path:
            return main_routine, functions
        for name, function in functions.items():
            if function == remaining_path[: len(function)]:
                result = self.partition_path(remaining_path[len(function) :], main_routine + (name,), functions)
                if result is not None:
                    return result
        if len(functions) < 3:
            return self.add_function(remaining_path, main_routine, functions)
        return None

    def add_function(
        self, remaining_path: tuple[str, ...], main_routine: MainRoutine, functions: Functions
    ) -> tuple[MainRoutine, Functions] | None:
        name = "ABC"[len(functions)]
        for candidate_length in range(1, len(remaining_path) + 1):
            candidate = remaining_path[:candidate_length]
            if len("".join(candidate)) > 20:
                break
            if candidate in functions.values():
                continue
            new_functions = functions.copy()
            new_functions[name] = candidate
            result = self.partition_path(remaining_path[candidate_length:], main_routine + (name,), new_functions)
            if result is not None:
                return result
        return None


# The scaffolding for my puzzle input
# ............###########..........................
# ............#.........#..........................
# ............#.........#..........................
# ............#.........#..........................
# ............#.........#..........................
# ............#.........#..........................
# ............#.........#########..................
# ............#.................#..................
# ......#########...............#..................
# ......#.....#.#...............#..................
# ......#.....#.#...............#..................
# ......#.......#...............#..................
# ......#.......#...............#..................
# ......#.......#...............#..................
# ......#.......#########.......#########..........
# ......#...............#...............#..........
# ^######...........#######.............#..........
# ..................#...#.#.............#..........
# ..................#...#.#.............#..........
# ..................#...#.#.............#..........
# ..................#.#####.............###########
# ..................#.#.#.........................#
# ..................#####.........................#
# ....................#...........................#
# ....................#...........................#
# ....................#...........................#
# ....................#...........................#
# ....................#...........................#
# ..............#######...........................#
# ..............#.................................#
# ..............#...........................#######
# ..............#...........................#......
# ..............#...........................#......
# ..............#...........................#......
# ..............#...........................#......
# ..............#...........................#......
# ..............#...#####.................#####....
# ..............#...#...#.................#.#.#....
# ..............###########.............#####.#....
# ..................#...#.#.............#.#...#....
# ..................#...#########.......#.#...#....
# ..................#.....#.....#.......#.#...#....
# ..................#######.....#.......#######....
# ..............................#.........#........
# ..............................#.........#........
# ..............................#.........#........
# ..............................###########........
