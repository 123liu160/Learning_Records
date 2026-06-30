# ，数组有重复数字，要求返回所有不重复的子集。
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()  # 必须排序，让重复数字挨在一起

        def backtrack(start):
            # 子集：每一步都保存
            res.append(path.copy())

            # 从 start 往后选
            for i in range(start, len(nums)):
                # 去重核心：同一层跳过重复数字
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # 选择
                path.append(nums[i])
                # 递归
                backtrack(i + 1)
                # 回溯
                path.pop()

        backtrack(0)
        return res