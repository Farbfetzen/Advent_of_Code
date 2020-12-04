# https://adventofcode.com/2020/day/4


REQUIRED = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")  # no "cid"


def part_1(passports):
    n_valid = 0
    for passport in passports:
        if all(req in passport for req in REQUIRED):
            n_valid += 1
    return n_valid


def part_2(passports):
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
        valid_hcl = "0123456789abcdef"
        if (hcl[0] != "#"
                or len(hcl) != 7
                or any(x not in valid_hcl for x in hcl[1:])):
            continue

        valid_ecl = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        if not passport["ecl"] in valid_ecl:
            continue

        pid = passport["pid"]
        if len(pid) != 9 or any(n not in "0123456789" for n in pid):
            continue

        n_valid += 1
    return n_valid


with open("day_04_input.txt", "r") as file:
    passports = []
    for passport_str in file.read().split("\n\n"):
        passport = {}
        for field in passport_str.split():
            k, v = field.split(":")
            passport[k] = v
        passports.append(passport)

print(part_1(passports))  # 208
print(part_2(passports))  # 167
