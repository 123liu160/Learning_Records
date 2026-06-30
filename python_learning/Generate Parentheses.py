# 给定一个整数 n，返回所有格式正确的由 n 对括号组成的组合。
# 格式正确：括号必须合法闭合，不能出现 )() 这种错误情况
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        # backtrack(当前字符串, 左括号数, 右括号数)
        def backtrack(s, left, right):
            # 终止条件：长度满了（2*n），保存结果
            if len(s) == 2 * n:
                res.append(s)
                return

            # 1. 可以加左括号：只要没超过 n
            if left < n:
                backtrack(s + "(", left + 1, right)

            # 2. 可以加右括号：必须 右 < 左
            if right < left:
                backtrack(s + ")", left, right + 1)

        # 从空串、0左0右开始
        backtrack("", 0, 0)
        return res