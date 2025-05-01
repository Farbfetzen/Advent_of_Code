#!/usr/bin/env python3

"""Creates script and test templates and downloads the input for a given day.
The optional arguments are 'year' and 'day' with the current year and day as default values.
Example: ./prepare.py 2020 7
You can also run it with the argument --all-inputs to download all inputs you don't yet have.
"""

import argparse
import datetime
import itertools
import os

import requests

from src.util import date_args


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
URL = "https://adventofcode.com/{year}/day/{day}"
THIS_PATH = os.path.dirname(os.path.realpath(__file__))
SCRIPT_PATH = os.path.join("src", "year{year}", "day{day_padded}.py")
TEST_PATH = os.path.join("test", "year{year}", "test_day{day_padded}.py")
COOKIE_PATH = os.path.abspath(os.path.join(THIS_PATH, "../session_cookie.txt"))


class Preparer:

    def __init__(self, year: int, day: int):
        self.year = str(year)
        self.day = str(day).zfill(2)
        self.url = f"https://adventofcode.com/{self.year}/day/{day}"
        self.input_year_dir = os.path.abspath(os.path.join(THIS_PATH, "../input", f"{self.year}"))

    def prepare_all(self) -> None:
        self.prepare_input()
        self.prepare_sample()
        self.prepare_script()
        self.prepare_test()

        print("\nDone. Have fun!")
        print(self.url, end="\n\n")

    def prepare_input(self) -> bool:
        """Download the input and write it to file.
        Returns True on success and False on failure.
        """
        input_path = os.path.join(self.input_year_dir, f"{self.day}-input.txt")
        if not os.path.exists(self.input_year_dir):
            os.mkdir(self.input_year_dir)
        elif self.check_file_exists(input_path, "input"):
            return True

        # Remember that the session cookie expires after some time. You can get
        # the current one from the website while being logged in.
        with open(COOKIE_PATH) as file:
            cookie = file.read().strip()

        input_url = self.url + "/input"
        print(f"Downloading input from {input_url}")
        response = requests.get(input_url, cookies={"session": cookie}, timeout=5)
        if response.ok:
            print("Writing input file.")
            with open(input_path, "w") as file:
                file.write(response.text)
        else:
            print("Error! Got status: ", response.status_code)
            print(response.text)
            if "log in" in response.text:
                print("Maybe the session cookie expired?")
            print("\nCreating empty file for you to paste the input manually.")
            open(input_path, "w").close()
        self.print_file_link(input_path)
        return response.ok

    def prepare_sample(self) -> None:
        sample_path = os.path.join(self.input_year_dir, f"{self.day}-sample.txt")
        if not os.path.exists(self.input_year_dir):
            os.mkdir(self.input_year_dir)
        elif self.check_file_exists(sample_path, "sample"):
            return
        print("Creating sample file.")
        open(sample_path, "w").close()
        self.print_file_link(sample_path)

    def prepare_script(self) -> None:
        year_path = os.path.join("src", f"year_{self.year}")
        solution_path = os.path.join(year_path, f"day_{self.day}.py")
        if not os.path.exists(year_path):
            os.mkdir(year_path)
        elif self.check_file_exists(solution_path, "solution"):
            return
        solution_template = SOLUTION_TEMPLATE.format(url=self.url, year=self.year, day=self.day)
        print("Creating solution file.")
        with open(solution_path, "w") as file:
            file.write(solution_template)
        self.print_file_link(solution_path)

    def prepare_test(self) -> None:
        test_path = os.path.join("test", f"test_{self.year}.py")
        if self.check_file_exists(test_path, "test"):
            return
        test_template = TEST_TEMPLATE.format(year=self.year)
        print("Creating test file.")
        with open(test_path, "w") as file:
            file.write(test_template)
        self.print_file_link(test_path)

    def check_file_exists(self, path: str, name: str) -> bool:
        if os.path.exists(path):
            print(f"Skipping {name} file generation because it already exists.")
            self.print_file_link(path)
            return True
        return False

    @staticmethod
    def print_file_link(path: str) -> None:
        # This link should be clickable in the console.
        print(f"file://{os.path.abspath(path)}")


def load_all_inputs() -> None:
    print("Attempting to download the inputs of all challenges you don't already have. Are you sure? (y/N)")
    decision = input("> ")
    if not decision.lower().startswith("y"):
        print("Aborting.")
        return
    today = datetime.date.today()
    year_day = itertools.product(range(2015, today.year + 1), range(1, 26))
    for year, day in year_day:
        if datetime.date(year, 12, day) > today:
            return
        ok = Preparer(year, day).prepare_input()
        if not ok:
            print(f"Something went wrong! {year=}, {day=}")
            return


def main() -> None:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    date_args.add_date_args(parser)
    parser.add_argument("--all-inputs", action="store_true")
    args = parser.parse_args()
    if args.all_inputs:
        load_all_inputs()
    else:
        year, day = date_args.validate_args(args.year, args.day)
        Preparer(year, day).prepare_all()


main()
