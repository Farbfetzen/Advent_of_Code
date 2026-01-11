# https://adventofcode.com/2020/day/4

import re
from typing import Callable

from src.util.inputs import Inputs
from src.util.solution import Solution


type Passport = dict[str, str]


class Solution2020Day04(Solution):
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}  # no "cid"
    height_pattern = re.compile(r"^(?P<height>\d+)(?P<unit>[a-z]+)$")
    hair_color_pattern = re.compile("^#[0-9a-f]{6}$")
    valid_eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    def solve(self, inputs: Inputs) -> None:
        passports = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(passports))

        passports = self.prepare(inputs.input)
        self.result_1 = self.solve_1(passports)
        self.result_2 = self.solve_2(passports)

    @staticmethod
    def prepare(data: str) -> list[Passport]:
        passports = []
        for entry in data.split("\n\n"):
            passport = dict(field.split(":") for field in entry.split())  # noqa: S7494
            passports.append(passport)
        return passports

    def solve_1(self, passports: list[Passport]) -> int:
        return sum(1 for passport in passports if self.validate_required_fields(passport))

    def solve_2(self, passports: list[Passport]) -> int:
        validators = [
            self.validate_required_fields,
            self.validate_years,
            self.validate_height,
            self.validate_hair_color,
            self.validate_eye_color,
            self.validate_id
        ]
        return sum(all(validate(passport) for validate in validators) for passport in passports)

    def validate_passport(self, passport: Passport, validators: list[Callable[[Passport], bool]]) -> bool:
        return (all(req in passport for req in self.required_fields)
                and all(validate(passport) for validate in validators))

    def validate_required_fields(self, passport: Passport) -> bool:
        return self.required_fields.issubset(passport.keys())

    @staticmethod
    def validate_years(passport: Passport) -> bool:
        return ((1920 <= int(passport["byr"]) <= 2002)
                and (2010 <= int(passport["iyr"]) <= 2020)
                and (2020 <= int(passport["eyr"]) <= 2030))

    def validate_height(self, passport: Passport) -> bool:
        match = self.height_pattern.match(passport["hgt"])
        if match is None:
            return False
        height = int(match.group("height"))
        unit = match.group("unit")
        return (unit == "cm" and 150 <= height <= 193) or (unit == "in" and 59 <= height <= 76)

    def validate_hair_color(self, passport: Passport) -> bool:
        return self.hair_color_pattern.match(passport["hcl"]) is not None

    def validate_eye_color(self, passport: Passport) -> bool:
        return passport["ecl"] in self.valid_eye_colors

    @staticmethod
    def validate_id(passport: Passport) -> bool:
        pid = passport["pid"]
        return len(pid) == 9 and pid.isdigit()
