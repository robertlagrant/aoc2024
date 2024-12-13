from functools import cmp_to_key

from inputs import REAL_INPUT as INPUT

def parse(raw_input):
    raw_rules, raw_pages = raw_input.split("\n\n")
    rules: dict[tuple[str, str], int] = {}
    for raw_rule in raw_rules.split("\n"):
        prepage, postpage = raw_rule.split("|")
        rules[(prepage, postpage)] = 1
        rules[(postpage, prepage)] = -1
    
    rules_key_function = cmp_to_key(lambda a, b: rules.get((a, b), rules.get((b, a), 0)))    
    pages = [raw_page.split(",") for raw_page in raw_pages.split("\n")]

    return rules_key_function, pages


def filter_pages(rules_key_function, pages, valid_or_not):
    return [
        page for page in pages
        if (sorted(page, key=rules_key_function, reverse=True) == page) is valid_or_not
    ]


def part1(rules_key_function, pages):
    return sum(int(valid[len(valid)//2]) for valid in filter_pages(rules_key_function, pages, True))


def part2(rules_key_function, pages):
    return sum(
        int((new_invalid := sorted(invalid, key=rules_key_function, reverse=True))[len(new_invalid) // 2])
        for invalid in filter_pages(rules_key_function, pages, False)
    )


print(f"Part 1: {part1(*parse(INPUT))}")
print(f"Part 2: {part2(*parse(INPUT))}")
