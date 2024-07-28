#!/usr/bin/env python3

"""Creates script and test templates and downloads the input for a given day.
The optional arguments are 'year' and 'day' with the current year and day as default values.
Example: ./prepare.py 2020 7
You can also run it with the argument --all-inputs to download all inputs.
"""

import argparse
import datetime
import itertools
import os

import requests

from src.util.date_args import add_date_args, validate_args_default_today


SCRIPT_TEMPLATE = """# {url}\n
from src.util.types import Data, Solution\n\n
def prepare_data(data: str) -> str:
    return data\n\n
def part_1(data: str) -> None:
    return\n\n
# def part_2(data: str) -> None:
#     return\n\n
def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    # solution.samples_part_2.append(part_2(sample_data))\n
    # challenge_data = prepare_data(data.input)
    # solution.part_1 = part_1(challenge_data)
    # solution.part_2 = part_2(challenge_data)
    return solution
"""
TEST_TEMPLATE = """from unittest import TestCase\n
from src.util.load_data import load_data
from src.year{year}.day{day_padded} import part_1, part_2, prepare_data
from test.decorators import sample\n\n
data = load_data({year}, {day})\n\n
@sample
class Test{year}Day{day_padded}Samples(TestCase):\n
    prepared_data: str\n
    @classmethod
    def setUpClass(cls) -> None:
        cls.prepared_data = prepare_data(data.samples[0])\n
    def test_part_1(self) -> None:
        self.assertEqual(None, part_1(self.prepared_data))\n
    # def test_part_2(self) -> None:
    #     self.assertEqual(None, part_2(self.prepared_data))\n\n
# class Test{year}Day{day_padded}(TestCase):\n#
#     prepared_data: str\n#
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.prepared_data = prepare_data(data.input)\n#
#     def test_part_1(self) -> None:
#         self.assertEqual(None, part_1(self.prepared_data))\n#
#     def test_part_2(self) -> None:
#         self.assertEqual(None, part_2(self.prepared_data))
"""
URL = "https://adventofcode.com/{year}/day/{day}"
THIS_PATH = os.path.dirname(os.path.realpath(__file__))
SCRIPT_PATH = os.path.join("src", "year{year}", "day{day_padded}.py")
TEST_PATH = os.path.join("test", "year{year}", "test_day{day_padded}.py")
COOKIE_PATH = os.path.abspath(os.path.join(THIS_PATH, "../session_cookie.txt"))


class Preparer:

    def __init__(self, year: int, day: int):
        self.year = str(year)
        self.day = str(day)
        self.day_padded = self.day.zfill(2)
        self.url = f"https://adventofcode.com/{self.year}/day/{self.day}"
        self.input_year_dir = os.path.abspath(os.path.join(THIS_PATH, "../input", f"{self.year}"))

    def prepare_all(self) -> None:
        self.prepare_input()
        self.prepare_sample()
        self.prepare_script()
        self.prepare_test()

        print("\nDone. Have fun!")
        print(self.url, end="\n\n")

    def prepare_input(self) -> bool:
        input_path = os.path.join(self.input_year_dir, f"{self.day_padded}-input.txt")
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
        sample_path = os.path.join(self.input_year_dir, f"{self.day_padded}-sample.txt")
        if not os.path.exists(self.input_year_dir):
            os.mkdir(self.input_year_dir)
        elif self.check_file_exists(sample_path, "sample"):
            return
        print("Creating sample file.")
        open(sample_path, "w").close()
        self.print_file_link(sample_path)

    def prepare_script(self) -> None:
        src_year_path = os.path.join("src", f"year{self.year}")
        script_path = os.path.join(src_year_path, f"day{self.day_padded}.py")
        if not os.path.exists(src_year_path):
            os.mkdir(src_year_path)
        elif self.check_file_exists(script_path, "script"):
            return
        script_template = SCRIPT_TEMPLATE.format(url=self.url)
        print("Writing script file.")
        with open(script_path, "w") as file:
            file.write(script_template)
        self.print_file_link(script_path)

    def prepare_test(self) -> None:
        test_year_path = os.path.join("test", f"year{self.year}")
        test_path = os.path.join(test_year_path, f"test_day{self.day_padded}.py")
        if not os.path.exists(test_year_path):
            os.mkdir(test_year_path)
        elif self.check_file_exists(test_path, "test"):
            return
        test_template = TEST_TEMPLATE.format(day=self.day, day_padded=self.day_padded, year=self.year)
        print("Writing test file.")
        with open(test_path, "w") as file:
            file.write(test_template)
        self.print_file_link(test_path)

    @staticmethod
    def check_file_exists(path: str, name: str) -> bool:
        if os.path.exists(path):
            print(f"Skipping {name} file generation because it already exists.")
            Preparer.print_file_link(path)
            return True
        return False

    @staticmethod
    def print_file_link(path: str) -> None:
        # This link should be clickable in the console.
        print(f"file://{os.path.abspath(path)}")


def load_all_inputs() -> None:
    print("Attempting to download the inputs of all past challenges. Are you sure? (y/N)")
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
    add_date_args(parser)
    parser.add_argument("--all-inputs", action="store_true")
    args = parser.parse_args()
    if args.all_inputs:
        load_all_inputs()
    else:
        year, day = validate_args_default_today(args.year, args.day)
        Preparer(year, day).prepare_all()


if __name__ == "__main__":
    main()
