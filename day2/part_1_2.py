import operator

from inputs import REAL_INPUTS as INPUTS

def parse(raw_inputs: str):
    return [[int(string_col) for string_col in raw_input.split()] for raw_input in raw_inputs.split("\n")]


def all_asc_desc(_input: list[int], op, within=3) -> bool:
    last_number = None
    for i in _input:
        if last_number is not None and (op(i, last_number) or within < abs(last_number - i)):
            return False
        last_number = i

    return True


def part1(inputs: list[list[int]]):
    return sum(all_asc_desc(_input, operator.ge) or all_asc_desc(_input, operator.le) for _input in inputs)


def part2(inputs: list[list[int]]):
    valid_count = 0
    for _input in inputs:
        skip_index = -1
        valid = False

        while not valid and skip_index < len(_input):
            temp_input = [el for i, el in enumerate(_input) if i == -1 or i != skip_index]
            valid = all_asc_desc(temp_input, operator.ge) or all_asc_desc(temp_input, operator.le)
            skip_index += 1
        
        if valid:
            valid_count += 1
    
    return valid_count
            

print(f"Part 1: {part1(parse(INPUTS))}")
print(f"Part 2: {part2(parse(INPUTS))}")
