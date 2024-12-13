from functools import cmp_to_key

from inputs import REAL_INPUT as INPUT

def parse(raw_input):
    raw_rules, raw_pages = raw_input.split("\n\n")
    rules: dict[tuple[str, str], int] = {}
    for raw_rule in raw_rules.split("\n"):
        prepage, postpage = raw_rule.split("|")
        rules[(prepage, postpage)] = 1
        rules[(postpage, prepage)] = -1
    
    pages = [raw_page.split(",") for raw_page in raw_pages.split("\n")]
    rules_key_function = cmp_to_key(lambda a, b: rules.get((a, b), rules.get((b, a), 0)))  

    valids = [page for page in pages if (sorted(page, key=rules_key_function, reverse=True) == page)]
    invalids = [page for page in pages if (sorted(page, key=rules_key_function, reverse=True) != page)]
  
    return valids, invalids, rules_key_function


def part1(valids, invalids, rules_key_function):
    return sum(int(valid[len(valid)//2]) for valid in valids)


def part2(valids, invalids, rules_key_function):
    return sum(
        int((new_invalid := sorted(invalid, key=rules_key_function, reverse=True))[len(new_invalid) // 2])
        for invalid in invalids
    )


print(f"Part 1: {part1(*parse(INPUT))}")
print(f"Part 2: {part2(*parse(INPUT))}")
