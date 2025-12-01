from inputs import REAL_INPUT as INPUT


def part1(haystack: list[str], needle: str):
    return sum(
        all(haystack[j + m*dj][i+ m*di] == expected_letter for m, expected_letter in enumerate(needle[1:], start=1))
        for j in range(len(haystack))
        for i in range(len(haystack[j]))
        for di, dj in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        if haystack[j][i] == needle[0]
        if 0 <= i + 3 * di < len(haystack[j])
        if 0 <= j + 3 * dj < len(haystack)
    )


def part2(letters: list[str]):
    return sum(
        1
        for j in range(1, len(letters) - 1)
        for i in range(1, len(letters[j]) - 1)
        if letters[j][i] == "A"
        if set((letters[j-1][i+1], letters[j+1][i-1])) == set((letters[j-1][i-1], letters[j+1][i+1])) == set("SM")
    )


print(f"Part 1: {part1(INPUT.split("\n"), "XMAS")}")
print(f"Part 2: {part2(INPUT.split("\n"))}")
