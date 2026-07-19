# 给定一个二维网格 grid，网格中字符 '1' 代表陆地，'0' 代表水域，请统计并返回岛屿的总数量。
# 岛屿的定义：由水平或竖直相邻的陆地相连形成，四周被水域包围。你可以假设网格四周全是水域（即网格所有边界外侧都是水）。
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(i, j):
            # Boundary check or water, stop recursion
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "0":
                return
            # Mark current land as visited
            grid[i][j] = "0"
            # Four directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count