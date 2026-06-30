# 给定一个字符串 s，将 s 分割成一些子串，使得每个子串都是回文串。
# 返回所有可能的分割方案。
# 回文串：正读和反读都一样的字符串，如 a, aa, aba。
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []  # 存放最终所有分割方案
        path = []  # 存放当前的分割结果

        # 回溯函数：start 表示从哪个索引开始切
        def backtrack(start):
            # 1. 终止条件：切到最后了，保存方案
            if start >= len(s):
                res.append(path.copy())
                return

            # 2. 遍历所有可能的切割点
            for i in range(start, len(s)):
                # 3. 截取子串：s[start ... i]
                substr = s[start: i + 1]

                # 4. 判断是不是回文，不是就跳过（剪枝）
                if substr == substr[::-1]:  # 最简单的回文判断
                    path.append(substr)  # 是回文，加入当前方案
                    backtrack(i + 1)  # 继续切下一段
                    path.pop()  # 回溯：撤销选择

        # 从第 0 位开始切
        backtrack(0)
        return res