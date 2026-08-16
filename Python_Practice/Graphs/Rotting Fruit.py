# 给定二维矩阵 grid，每个单元格有三种取值：0 代表空单元格，1 代表新鲜水果，2 代表腐烂水果；
# 每过一分钟，与腐烂水果上下左右相邻的新鲜水果就会变成腐烂水果，请返回全部新鲜水果腐烂完毕所需的最少分钟数
# 若无法全部腐烂则返回 - 1。
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0

        # 统计新鲜水果数量，所有腐烂水果入队列
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # 没有新鲜水果，直接返回0
        if fresh == 0:
            return 0

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time = 0

        # BFS层序遍历，一层代表一分钟
        while q and fresh > 0:
            level_size = len(q)
            for _ in range(level_size):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    # 遇到新鲜水果，将其腐烂
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            time += 1

        return time if fresh == 0 else -1