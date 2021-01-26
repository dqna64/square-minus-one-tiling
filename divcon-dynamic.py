import numpy as np


def draw_grid(ori, grid):
    global cnt
    # ori is a 2-tuple containing an integer [1, 4] and an array of 4 more 2-tuples
    arrow = ori[0]
    subArrows = ori[1]
    thisGridSize = len(grid)
    # Array not present if last recursion
    if len(subArrows) == 0:
        # Recursion exit point
        # The grid given must be 2x2
        cnt += 1
        if ori[0] == 1:
            grid[0, 0] = cnt
            grid[1, 0] = cnt
            grid[1, 1] = cnt
        elif ori[0] == 2:
            grid[0, 1] = cnt
            grid[1, 0] = cnt
            grid[1, 1] = cnt
        elif ori[0] == 3:
            grid[0, 0] = cnt
            grid[0, 1] = cnt
            grid[1, 1] = cnt
        elif ori[0] == 4:
            grid[0, 0] = cnt
            grid[0, 1] = cnt
            grid[1, 0] = cnt
        # grid modified in-place
        return

    # Continue recursion
    for i in range(0, 4):
        if i == 0:  # 1st quad
            draw_grid(subArrows[i], grid[:int(
                thisGridSize/2), int(thisGridSize/2):])
        elif i == 1:  # 2nd quad
            draw_grid(subArrows[i], grid[:int(
                thisGridSize/2), :int(thisGridSize/2)])
        elif i == 2:  # 3rd quad
            draw_grid(subArrows[i], grid[int(
                thisGridSize/2):, :int(thisGridSize/2)])
        elif i == 3:  # 4th quad
            draw_grid(subArrows[i], grid[int(
                thisGridSize/2):, int(thisGridSize/2):])


ori = (2, [(3, []), (1, []), (1, []), (2, [])])

grid_size = 4
grid = np.zeros((grid_size, grid_size))

cnt = 0
draw_grid(ori, grid)
print(grid)
