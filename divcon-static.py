import numpy as np
import sys
sys.setrecursionlimit(1500)


def place(p1x, p1y, p2x, p2y, p3x, p3y):
    p1x, p1y, p2x, p2y, p3x, p3y = [
        int(coord) for coord in (p1x, p1y, p2x, p2y, p3x, p3y)]
    global cnt
    cnt += 1
    grid[p1x, p1y] = cnt
    grid[p2x, p2y] = cnt
    grid[p3x, p3y] = cnt


def tile(n, corner):
    global cnt
    x, y = [int(coord) for coord in corner]

    if n == 2:
        cnt += 1
        for i in range(0, n):
            for j in range(0, n):
                if grid[x+i][y+j] == 0:
                    grid[x+i][y+j] = cnt
        return

    # Find 'hole' location ( not necessarily the actual hole, just the gap within this segment)
    for i in range(x, x+n):
        for j in range(y, y+n):
            if grid[i][j] != 0:
                r = i
                c = j

    # If missing tile is in 2nd quadrant CORRECT
    if (r < x + n / 2 and c < y + n / 2):
        place(x + n / 2, y + (n / 2) - 1, x + n / 2,
              y + n / 2, x + n / 2 - 1, y + n / 2)

    # If missing Tile is in 3rd quadrant
    elif (r >= x + n / 2 and c < y + n / 2):
        place(x + n / 2, y + (n / 2),
              x + n / 2 - 1, y + n / 2 - 1,
              x + n / 2 - 1, y + n / 2)

    # If missing Tile is in 1st quadrant
    elif (r < x + n / 2 and c >= y + n / 2):
        place(x + (n / 2) - 1, y + (n / 2) - 1, x + (n / 2),
              y + n / 2 - 1, x + (n / 2), y + (n / 2))

    # If missing Tile is in 4th quadrant CORRECT
    elif (r >= x + n / 2 and c >= y + n / 2):
        place(x + (n / 2) - 1, y + (n / 2), x + (n / 2),
              y + (n / 2) - 1, x + (n / 2) - 1,
              y + (n / 2) - 1)

    # diving it again in 4 quadrants
    tile(int(n / 2), (x, y + n / 2))
    tile(int(n / 2), (x, y))
    tile(int(n / 2), (x + n / 2, y))
    tile(int(n / 2), (x + n / 2, y + n / 2))


grid_size = 8  # number of tiles on side, a power of 2 min 2
grid = np.zeros((grid_size, grid_size), dtype=np.int8)

hole = (0, 3)
cnt = 0
grid[hole] = -1

tile(grid_size, (0, 0))
print(grid)
