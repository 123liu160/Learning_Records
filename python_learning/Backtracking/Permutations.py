# 给定一个包含互不相同整数的数组 nums，返回其所有可能的排列。你可以按任意顺序返回答案。
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []  # 存放最终所有排列
        used = [False] * len(nums)  # 标记数字是否被用过

        def backtrack(path):
            # 终止条件：当前排列长度 == 原数组长度 → 完成一个排列
            if len(path) == len(nums):
                res.append(path.copy())
                return

            # 排列必须每次从头遍历
            for i in range(len(nums)):
                if used[i]:  # 跳过已经选过的数字
                    continue

                used[i] = True  # 标记为已使用
                path.append(nums[i])  # 加入当前排列

                backtrack(path)  # 继续选下一个数字

                path.pop()  # 回溯撤销选择
                used[i] = False  # 取消标记

        backtrack([])  # 从空路径开始
        return res