from collections import Counter

from inputs import TEST_INPUT, REAL_INPUT


def parse(parse_input):
    nums = [(left, right) for left, right in [map(int, pair.split()) for pair in parse_input.split("\n")]]

    return [[nums[j][i] for j in range(len(nums))] for i in range(len(nums[0]))]


def part1(lefts, rights):
    return sum(abs(left - right) for left, right in zip(sorted(lefts), sorted(rights)))


def part2(lefts, rights):
    rights_counts = Counter(rights)

    return sum(left * rights_counts[left] for left in lefts)


print(f"Part 1: {part1(*parse(REAL_INPUT))}")
print(f"Part 2: {part2(*parse(REAL_INPUT))}")
