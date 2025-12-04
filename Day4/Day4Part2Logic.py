from copy import deepcopy

NEIGHBORS = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def find_accessible_positions(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    accessible = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue
            adj = 0
            for dr, dc in NEIGHBORS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                    adj += 1
                    if adj >= 4:
                        break
            if adj < 4:
                accessible.append((r, c))
    return accessible

def total_removed_by_forklifts(grid):
    mutable = [list(row) for row in grid]
    total_removed = 0
    round_num = 0

    while True:
        accessible = find_accessible_positions(mutable)
        if not accessible:
            break
        round_num += 1
        for r, c in accessible:
            mutable[r][c] = '.'
        total_removed += len(accessible)

    final_grid = ["".join(row) for row in mutable]
    return total_removed, final_grid

if __name__ == "__main__":
    with open("Day4/Day4Input.txt") as f:
        grid = [line.rstrip("\n") for line in f if line.rstrip("\n") != ""]

    removed, final = total_removed_by_forklifts(grid)
    print()
    print("Total removed:", removed)
