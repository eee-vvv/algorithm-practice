def largest1BorderedSquare(grid: list[list[int]]) -> int:
    Tab = namedtuple('Tab', ['left', 'up'])
    tab = [[None] * len(grid[0]) for _ in grid]

    tab[0][0] = Tab(grid[0][0], grid[0][0])

    i = 0
    for j in range(1, len(grid[0])):
        numleft = tab[i][j-1].left + 1 if grid[i][j] == 1 else 0
        numup = 1 if grid[i][j] == 1 else 0
        tab[i][j] = Tab(numleft, numup)

    j = 0
    for i in range(1, len(grid)):
        numleft = 1 if grid[i][j] == 1 else 0
        numup = tab[i-1][j].up + 1 if grid[i][j] == 1 else 0
        tab[i][j] = Tab(numleft, numup)

    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            numleft = tab[i][j-1].left + 1 if grid[i][j] == 1 else 0
            numup = tab[i-1][j].up + 1 if grid[i][j] == 1 else 0
            tab[i][j] = Tab(numleft, numup)

    # for each possible square
    maxsq = min(len(grid), len(grid[0]))
    for k in range(maxsq, 0, -1):
        for i in range(k - 1, len(grid)):
            for j in range(k - 1, len(grid[0])):
                # check the square...
                # check up from bot-right
                # check left from bot-right
                # check up from bot-left
                # check left from top-right

                if (tab[i][j].up >= k
                        and tab[i][j].left >= k 
                        and tab[i][j-k+1].up >= k
                        and tab[i-k+1][j].left >= k):
                    return k*k

    return 0
