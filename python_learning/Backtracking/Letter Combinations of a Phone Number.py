# 给你一个由数字 2~9 组成的字符串 digits。
# 每个数字对应一组字母（手机九宫格键盘）：
# 2: abc
# 3: def
# 4: ghi
# 5: jkl
# 6: mno
# 7: pqrs
# 8: tuv
# 9: wxyz
# 每个数字可以任选一个它对应的字母。
# 返回所有可能的字母组合。
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # 九宫格键盘映射
        key = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        # 回溯：index 是当前处理第几个数字
        def backtrack(index, path):
            # 终止条件：所有数字都处理完了
            if index == len(digits):
                res.append(path)
                return

            # 当前数字对应的所有字母
            current_digit = digits[index]
            letters = key[current_digit]

            # 遍历每个字母，选一个继续
            for c in letters:
                backtrack(index + 1, path + c)

        # 从第 0 个数字、空字符串开始
        backtrack(0, "")
        return res