from inputs import REAL_INPUT as INPUT

NEXT_DIRECTION = {
   (-1, 0): (0, 1),
   (0, 1): (1, 0),
   (1, 0): (0, -1),
   (0, -1): (-1, 0),
}

def parse(lines: list[str]):
    row_count, col_count = len(lines), len(lines[0])
    barriers = set()
    for row_index, line in enumerate(lines):
        for col_index, c in enumerate(line):
            if c == "#":
                barriers.add((row_index, col_index))
            elif c == "^":
                start = (row_index, col_index)
    
    return row_count, col_count, barriers, start
    

direction = (-1, 0)
row_count, col_count, barriers, start = parse(INPUT.split("\n"))
trail_vectors = [(start, direction)]

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

print(trail_vectors)
print(len(set([position for position, _ in trail_vectors])))

def print_it():
    for row_i in range(row_count):
        row = []
        for col_i in range(col_count):
            if ((row_i, col_i), direction) in trail_vectors:
                row.append("X")
            elif (row_i, col_i) in barriers:
                row.append("#")
            else:
                row.append(".")
        print("".join(row))
    
print_it()