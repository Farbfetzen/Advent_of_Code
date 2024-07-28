# https://adventofcode.com/2020/day/16

from re import findall
from typing import Any

from src.util.types import Data, Solution


def prepare_data(data: str) -> dict[str, Any]:
    rules_str, my_ticket_str, other_tickets_str = data.split("\n\n")
    rules = {}
    for line in rules_str.splitlines():
        field = line.split(":")[0]
        low1, high1, low2, high2 = (int(x) for x in findall(r"(\d+)", line))
        allowed_values = set(range(low1, high1+1)) | set(range(low2, high2+1))
        rules[field] = allowed_values
    my_ticket = tuple(int(x) for x in my_ticket_str.splitlines()[1].split(","))
    other_tickets = tuple(tuple(int(x) for x in line.split(","))
                          for line in other_tickets_str.splitlines()[1:])
    return {
        "rules": rules,
        "my_ticket": my_ticket,
        "other_tickets": other_tickets
    }


def part_1(data):
    valid_values = set()
    for values in data["rules"].values():
        valid_values.update(values)
    sum_invalid = 0
    discard = set()
    for i, ticket in enumerate(data["other_tickets"]):
        invalid = set(ticket).difference(valid_values)
        if invalid:
            sum_invalid += sum(invalid)
            discard.add(i)
    data["other_tickets"] = tuple(x for i, x in enumerate(data["other_tickets"])
                                  if i not in discard)
    return sum_invalid


def part_2(data):
    # Depends on part_1() to first remove all invalid tickets.
    columns = tuple({x} for x in data["my_ticket"])
    for i in range(len(columns)):
        for ticket in data["other_tickets"]:
            columns[i].add(ticket[i])
    possible_fields = []
    for col in columns:
        names = set()
        for field_name, valid_values in data["rules"].items():
            if valid_values.issuperset(col):
                names.add(field_name)
        possible_fields.append(names)

    # Search for entries where only one field is possible and remove that
    # from all other possible positions.
    fixed_fields = [p.pop() if len(p) == 1 else "" for p in possible_fields]
    while not all(fixed_fields):
        for f in fixed_fields:
            for i, p in enumerate(possible_fields):
                if f in p:
                    p.remove(f)
                if len(p) == 1:
                    fixed_fields[i] = p.pop()

    result = 1
    for i, f in enumerate(fixed_fields):
        if f.startswith("departure"):
            result *= data["my_ticket"][i]
    return result


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
