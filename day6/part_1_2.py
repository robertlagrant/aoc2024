from inputs import REAL_INPUT as INPUT

NEXT_DIRECTION = {
   (-1, 0): (0, 1),
   (0, 1): (1, 0),
   (1, 0): (0, -1),
   (0, -1): (-1, 0),
}

def parse(lines: list[str]):
    row_count, col_count = len(lines), len(lines[0])
    barriers = set((row_index, col_index) for row_index, line in enumerate(lines) for col_index, c in enumerate(line) if c == "#")
    start = [(row_index, col_index) for row_index, line in enumerate(lines) for col_index, c in enumerate(line) if c == "^"][0]
    
    return row_count, col_count, barriers, start
    

def part1(row_count, col_count, barriers, start):
    row_count, col_count, barriers, start = parse(INPUT.split("\n"))
    trail_vectors = [(start, list(NEXT_DIRECTION.keys())[0])]

    while True:
        position, direction = trail_vectors[-1]
        next_row = position[0] + direction[0]
        next_col = position[1] + direction[1]
        if (next_row, next_col) in barriers:
            trail_vectors.append(((position[0], position[1]), NEXT_DIRECTION[direction]))
        elif next_row < 0 or next_row >= row_count or next_col < 0 or next_col >= col_count:
            break
        else:
            trail_vectors.append(((next_row, next_col), direction))
    
    return len(set([position for position, _ in trail_vectors]))

print(f"Part 1: {part1(*parse(INPUT.split("\n")))}")

