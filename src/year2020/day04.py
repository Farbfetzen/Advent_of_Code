# https://adventofcode.com/2020/day/4

from src.util.types import Data, Solution


REQUIRED = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")  # no "cid"


def prepare_data(data: str) -> list[dict[str, str]]:
    passports = []
    for entry in data.split("\n\n"):
        passport = {k: v for k, v in (field.split(":") for field in entry.split())}
        passports.append(passport)
    return passports


def part_1(passports):
    n_valid = 0
    for passport in passports:
        if all(req in passport for req in REQUIRED):
            n_valid += 1
    return n_valid


def part_2(passports):
    valid_hcl = "0123456789abcdef"
    valid_ecl = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    n_valid = 0
    for passport in passports:
        if not all(req in passport for req in REQUIRED):
            continue

        if not (1920 <= int(passport["byr"]) <= 2002):
            continue

        if not (2010 <= int(passport["iyr"]) <= 2020):
            continue

        if not (2020 <= int(passport["eyr"]) <= 2030):
            continue

        hgt = passport["hgt"]
        unit = hgt[-2:]
        if unit == "cm":
            if not (150 <= int(hgt[:-2]) <= 193):
                continue
        elif unit == "in":
            if not (59 <= int(hgt[:-2]) <= 76):
                continue
        else:
            continue

        hcl = passport["hcl"]
        if (hcl[0] != "#"
                or len(hcl) != 7
                or any(x not in valid_hcl for x in hcl[1:])):
            continue

        if not passport["ecl"] in valid_ecl:
            continue

        pid = passport["pid"]
        if len(pid) != 9 or any(n not in "0123456789" for n in pid):
            continue

        n_valid += 1

    return n_valid


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
