def count_accessible_rolls(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    neighbors = [
        (-1,-1), (-1,0), (-1,1),
        ( 0,-1),         ( 0,1),
        ( 1,-1), ( 1,0), ( 1,1),
    ]

    accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue

            adj = 0
            # count adjacent @
            for dr, dc in neighbors:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == "@":
                        adj += 1
                        if adj >= 4:
                            break

            if adj < 4:
                accessible += 1

    return accessible

with open("Day4/Day4Input.txt") as f:
    grid = [line.rstrip("\n") for line in f]

print(count_accessible_rolls(grid))
