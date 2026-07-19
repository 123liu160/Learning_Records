#给定一个二维矩阵网格 grid，网格中的每个元素是 0（代表水域）或 1（代表陆地）。
# 岛屿的定义：由若干横向或纵向相邻的 1 连接而成（斜向相连不算连通）。你可以假定网格四条外围边界外全是水域。
# 岛屿面积指该岛屿包含的单元格总数。
# 要求返回网格中岛屿的最大面积；若不存在任何岛屿，则返回 0
def maxAreaOfIsland(grid):
    if not grid or not grid[0]:
        return 0
    m = len(grid)
    n = len(grid[0])
    max_area = 0

    def dfs(x, y):
        # 越界 或 当前是水，面积为0
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
            return 0
        # 标记已访问
        grid[x][y] = 0
        # 当前格子1 + 上下左右四块面积
        return 1 + dfs(x+1, y) + dfs(x-1, y) + dfs(x, y+1) + dfs(x, y-1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                cur = dfs(i, j)
                max_area = max(max_area, cur)
    return max_area