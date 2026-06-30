# 给定一个二维字符网格 board 和一个字符串 word。
# 如果这个单词存在于网格中，返回 true，否则返回 false。
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        # 回溯函数：当前坐标 (i,j)，当前匹配到单词的第 k 位
        def backtrack(i, j, k):
            # 终止条件：k 等于单词长度 → 全部匹配成功
            if k == len(word):
                return True

            # 越界 / 字符不匹配 / 已经访问过 → 直接返回 false
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            if board[i][j] != word[k]:
                return False

            # 标记当前格子为已访问（临时改成特殊字符）
            temp = board[i][j]
            board[i][j] = '#'

            # 上下左右四个方向递归
            found = backtrack(i + 1, j, k + 1) or \
                    backtrack(i - 1, j, k + 1) or \
                    backtrack(i, j + 1, k + 1) or \
                    backtrack(i, j - 1, k + 1)

            # 回溯：恢复原来的字符
            board[i][j] = temp

            return found

        # 遍历每一个格子作为起点
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True

        return False