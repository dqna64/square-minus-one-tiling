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
        if arrow == 0:
            grid[0, 0] = cnt
            grid[1, 0] = cnt
            grid[1, 1] = cnt
        elif arrow == 1:
            grid[0, 1] = cnt
            grid[1, 0] = cnt
            grid[1, 1] = cnt
        elif arrow == 2:
            grid[0, 0] = cnt
            grid[0, 1] = cnt
            grid[1, 1] = cnt
        elif arrow == 3:
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


def generateOri(hole, grid_size):
    # Exit recursion
    if grid_size == 2:
        if hole == (0, 1):  # 1st quad
            return (0, [])
        elif hole == (0, 0):  # 2nd quad
            return (1, [])
        elif hole == (1, 0):  # 3rd quad
            return (2, [])
        elif hole == (1, 1):  # 4th quad
            return (3, [])

    holeQuad = None
    if hole[0] < grid_size/2 and hole[1] >= grid_size/2:  # 1st quad
        holeQuad = 0
    elif hole[0] < grid_size/2 and hole[1] < grid_size/2:  # 2nd quad
        holeQuad = 1
    elif hole[0] >= grid_size/2 and hole[1] < grid_size/2:  # 3rd quad
        holeQuad = 2
    elif hole[0] >= grid_size/2 and hole[1] >= grid_size/2:  # 4th quad
        holeQuad = 3
    else:
        raise NameError("hole is not inside grid!!!")

    subHoleQuads = []

    # Continue recursion
    for i in range(4):  # For each quadrant, in order 0, 1, 2, 3
        subHole = None
        if i == holeQuad:  # If we are in the quad with the hole
            if i == 0:  # 1st quad
                subHole = (hole[0], hole[1]-int(grid_size/2))
            elif i == 1:  # 2nd quad
                subHole = (hole[0], hole[1])
            elif i == 2:  # 3rd quad
                subHole = (hole[0]-int(grid_size/2), hole[1])
            elif i == 3:  # 4th quad
                subHole = (hole[0]-int(grid_size/2), hole[1]-int(grid_size/2))
        else:  # Otherwise
            # The subHole is just a pretend hole in opposite direction
            if i == 0:
                subHole = (int(grid_size/2)-1, 0)
            elif i == 1:
                subHole = (int(grid_size/2)-1, int(grid_size/2)-1)
            elif i == 2:
                subHole = (0, int(grid_size/2)-1)
            elif i == 3:
                subHole = (0, 0)
        print(i, subHole)
        subHoleQuads.append(generateOri(subHole, int(grid_size/2)))
    return (holeQuad, subHoleQuads)


# Test cases
# hole cartesian coords is (1, 2)
ori4 = (1, [(2, []), (0, []), (0, []), (1, [])])
ori8 = (1, [(2, [(2, []), (3, []), (2, []), (1, [])]),
            (1, [(3, []), (3, []), (0, []), (1, [])]),
            (0, [(0, []), (3, []), (0, []), (1, [])]),
            (1, [(2, []), (1, []), (0, []), (1, [])])
            ]
        )  # hole cartesian coords is (2, 4)

GRID_SIZE = 8
trueGrid = np.zeros((GRID_SIZE, GRID_SIZE))

trueHole = (0, 7)  # Be careful!! (cartx-1, carty-1)
# trueGrid[trueHole] = -1

ori = generateOri(trueHole, GRID_SIZE)

cnt = 0
draw_grid(ori, trueGrid)
print(ori)
print(trueGrid)
