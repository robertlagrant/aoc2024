from inputs import REAL_INPUTS as INPUT


def part1(letters: list[str]):
    x_coords = [(i, j) for j in range(len(letters)) for i in range(len(letters[j])) if letters[j][i] == "X"]

    return sum(
        all(letters[j + m*dj][i+ m*di] == expected_letter for m, expected_letter in enumerate("MAS", start=1))
        for i, j in x_coords
        for di, dj in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        if 0 <= i + 3 * di <= len(letters[j])-1
        if 0 <= j + 3 * dj <= len(letters)-1
    )


def part2(letters: list[str]):
    return sum(
        1
        for j in range(1, len(letters) - 1)
        for i in range(1, len(letters[j]) - 1)
        if letters[j][i] == "A"
        if set((letters[j-1][i+1], letters[j+1][i-1])) == set((letters[j-1][i-1], letters[j+1][i+1])) == set("SM")
    )


print(f"Part 1: {part1(INPUT.split("\n"))}")
print(f"Part 2: {part2(INPUT.split("\n"))}")
