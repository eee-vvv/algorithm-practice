from collections import namedtuple


def largest1BorderedSquare(grid: list[list[int]]) -> int:
    '''
    given a grid of 1s and 0s, return the area of the largest square within that grid that has a border of only 1s.
    '''
    # make a tabulation memo that represents each point in the grid
    # and its following information:
    # how many consecutive 1s it has to its left
    # how many consecutive 1s it has to its right
    Tab = namedtuple('Tab', ['left', 'up'])
    tab = [[None] * len(grid[0]) for _ in grid]
    
    # BOTTOM UP APPROACH:
    # start filling out our tabulation with the upper left corner
    # this have left and up values equal to the value of that point in the grid
    tab[0][0] = Tab(grid[0][0], grid[0][0])

    # fill out the top row of our tab
    # for each point if its grid value == 0 then so will it's left and up values
    # otherwise its left = 1 + the previous point's left
    i = 0
    for j in range(1, len(grid[0])):
        numleft = tab[i][j-1].left + 1 if grid[i][j] == 1 else 0
        numup = 1 if grid[i][j] == 1 else 0
        tab[i][j] = Tab(numleft, numup)

    # fill out the first column of our tab
    # for each point if its grid value == 0 then so will it's left and up values
    # otherwise its up = 1 + the previous point's up
    j = 0
    for i in range(1, len(grid)):
        numleft = 1 if grid[i][j] == 1 else 0
        numup = tab[i-1][j].up + 1 if grid[i][j] == 1 else 0
        tab[i][j] = Tab(numleft, numup)

    # fill in the rest of the tab using the same logic
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            numleft = tab[i][j-1].left + 1 if grid[i][j] == 1 else 0
            numup = tab[i-1][j].up + 1 if grid[i][j] == 1 else 0
            tab[i][j] = Tab(numleft, numup)

    # itterate through each possible square (going up and left) of a given point starting at the bottom right corner
    maxsq = min(len(grid), len(grid[0])) # the side length of biggest concievable square in our grid
    # itterate through all the possible square sizes starting at the biggest
    for k in range(maxsq, 0, -1):
        # itterate through all the points in the the area of our tab where:
        # they could be the bottom right corner of a square of size k
        for i in range(k - 1, len(grid)):
            for j in range(k - 1, len(grid[0])):
                
                # check the square to see if it has k or more runs of 1s at the following places...
                if (    # bottom-right corner: check up and left
                        tab[i][j].up >= k 
                        and tab[i][j].left >= k 
                        # bottom-left corner: check up
                        and tab[i][j-k+1].up >= k
                        # top-right corner: check left
                        and tab[i-k+1][j].left >= k
                    ):
                    # if it meets these criteria we have our square!
                    return k*k

    return 0
