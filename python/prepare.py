#!/usr/bin/env python3

"""Creates script and test templates and downloads the input for a given day.
The required positional arguments are 'year' and 'day'.
Example: ./prepare.py 2020 7
This script needs two environment variables to function:
- AOC_SESSION_COOKIE: The session cookie for authentication.
- AOC_USER_AGENT: Contact information where the advent of code maintainers can reach you.
  See https://www.reddit.com/r/adventofcode/wiki/faqs/automation
"""

import argparse
import datetime
import os
import sys
from dataclasses import dataclass
from pathlib import Path

import requests


SOLUTION_TEMPLATE = """# {url}

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution{year}Day{day}(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(prepared_input))
        self.sample_results_2.append(self.solve_2(prepared_input))

        prepared_input = self.prepare(inputs.input)
        self.result_1 = self.solve_1(prepared_input)
        self.result_2 = self.solve_2(prepared_input)

    @staticmethod
    def prepare(data: str) -> str:
        return data

    @staticmethod
    def solve_1(data: str) -> int:
        return 0

    @staticmethod
    def solve_2(data: str) -> int:
        return 0
"""

TEST_TEMPLATE = """from src import solutions
from src.util.inputs import load_inputs


def test_day_01() -> None:
    solution = solutions[{year}][1]()
    solution.solve(load_inputs({year}, 1))
    assert solution.sample_results_1[0] == 0
    assert solution.sample_results_2[0] == 0
    assert solution.result_1 == 0
    assert solution.result_2 == 0
"""

INIT_PY_TEMPLATE = """from typing import Type

from src.util.solution import Solution
from src.year_{year}.day_{day} import Solution{year}Day{day}


solutions_{year}: dict[int, Type[Solution]] = {{
    1: Solution{year}Day{day},
}}
"""

# The path of the directory where this script is located.
THIS_DIR = Path(__file__).resolve().parent


@dataclass
class Env:
    session_cookie: str = os.environ.get("AOC_SESSION_COOKIE") or ""
    user_agent: str = os.environ.get("AOC_USER_AGENT") or ""

    def __post_init__(self) -> None:
        missing_keys = []
        if not self.session_cookie:
            missing_keys.append("AOC_SESSION_COOKIE")
        if not self.user_agent:
            missing_keys.append("AOC_USER_AGENT")
        if missing_keys:
            sys.exit(f'Missing environment variable{'s' if len(missing_keys) > 1 else ''}: {", ".join(missing_keys)}')


def main() -> None:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)
    args = parser.parse_args()
    year = args.year
    day = args.day
    current_year = datetime.date.today().year
    if 2015 <= year <= current_year and 1 <= day <= 25:
        prepare(str(year), str(day), Env())
    else:
        sys.exit("Error: Invalid year or day.")


def prepare(year: str, day: str, env: Env) -> None:
    puzzle_url = f"https://adventofcode.com/{year}/day/{day}"
    day = day.zfill(2)
    input_dir = THIS_DIR.parent / "input" / f"{year}"

    prepare_input(input_dir, day, puzzle_url, env)
    prepare_sample(input_dir, day)
    prepare_solution(year, day, puzzle_url)
    prepare_test(year)

    print("\nDone. Have fun!")
    print(puzzle_url, end="\n\n")


def prepare_input(input_dir: Path, day: str, puzzle_url: str, env: Env) -> None:
    """Download the input and save it in a text file."""
    input_dir.mkdir(exist_ok=True)
    input_file = input_dir / f"{day}-input.txt"
    if input_file.exists():
        print("Skipping input file because it already exists.")
        print(input_file.as_uri())
        return

    input_url = puzzle_url + "/input"
    print(f"Downloading input from {input_url}")
    response = requests.get(
        input_url,
        headers={"user-agent": env.user_agent},
        cookies={"session": env.session_cookie},
        timeout=5,
    )
    if response.ok:
        print("Writing input file.")
        input_file.write_text(response.text)
    else:
        sys.exit(f"Error!\nResponse status: {response.status_code}\nResponse text: {response.text}")
    print(input_file.as_uri())


def prepare_sample(input_dir: Path, day: str) -> None:
    """Create an empty file for a sample input."""
    input_dir.mkdir(exist_ok=True)
    sample_file = input_dir / f"{day}-sample.txt"
    if sample_file.exists():
        print("Skipping sample file because it already exists.")
        print(sample_file.as_uri())
        return
    print("Creating sample file.")
    sample_file.touch()
    print(sample_file.as_uri())


def prepare_solution(year: str, day: str, puzzle_url: str) -> None:
    """Create a file containing a solution template."""
    year_dir = THIS_DIR / "src" / f"year_{year}"
    solution_file = year_dir / f"day_{day}.py"
    year_dir.mkdir(exist_ok=True)
    if solution_file.exists():
        print("Skipping solution file because it already exists.")
        print(solution_file.as_uri())
        return

    print("Creating solution file.")
    solution_file.write_text(SOLUTION_TEMPLATE.format(url=puzzle_url, year=year, day=day))
    print(solution_file.as_uri())

    init_py_file = year_dir / "__init__.py"
    if init_py_file.exists():
        return
    parent_init_py_file = THIS_DIR / "src" / "__init__.py"
    print(f"Creating __init__.py for {year}. Remember to add it to {parent_init_py_file.as_uri()}")
    init_py_file.write_text(INIT_PY_TEMPLATE.format(year=year, day=day))


def prepare_test(year: str) -> None:
    """Create a file containing a test template."""
    test_file = THIS_DIR / "test" / f"test_{year}.py"
    if test_file.exists():
        print("Skipping test file because it already exists.")
        print(test_file.as_uri())
        return
    print("Creating test file.")
    test_file.write_text(TEST_TEMPLATE.format(year=year))
    print(test_file.as_uri())


if __name__ == "__main__":
    main()
