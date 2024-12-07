import re

from inputs import REAL_INPUTS as INPUTS

PART_1_2_REGEX = r"(mul\((?P<mult_left>\d{1,3}),(?P<mult_right>\d{1,3})\)|(?P<do>do\(\))|(?P<do_not>don\'t\(\)))"


def part1(command: str):
    total = 0
    for match in re.finditer(PART_1_2_REGEX, command):
        values = match.groupdict()
        if values["mult_left"] is not None and values["mult_right"] is not None:
            total += int(values["mult_left"]) * int(values["mult_right"])
    
    return total


def part2(command: str):
    total = 0
    do_mult = True
    for match in re.finditer(PART_1_2_REGEX, command):
        values = match.groupdict()
        if values["do"] is not None:
            do_mult = True
        elif values["do_not"] is not None:
            do_mult = False
        elif do_mult is True:
            total += int(values["mult_left"]) * int(values["mult_right"])
    
    return total
            

print(f"Part 1: {part1(INPUTS)}")
print(f"Part 2: {part2(INPUTS)}")
