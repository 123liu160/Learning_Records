# 给定一个由互不相同整数组成的数组 nums 和一个目标整数 target，请你找出数组中所有唯一组合，使得组合内数字之和等于目标值。
# 数组中的同一个数字可以被重复选取无限次。
# 若两个组合里每个数字的出现次数完全一致，则视为同一组合；否则为不同组合。
# 你可以按任意顺序返回所有组合，组合内部的数字顺序也不作要求。
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.path = []

        def backtrack(start, cur_sum):
            # 1. 满足条件：保存结果
            if cur_sum == target:
                self.res.append(self.path.copy())
                return

            # 2. 和超了，直接回头
            if cur_sum > target:
                return

            # 3. 从 start 开始选（防重复）
            for i in range(start, len(nums)):
                # 选择
                self.path.append(nums[i])
                # 递归：可重复选 → 传 i，不是 i+1
                backtrack(i, cur_sum + nums[i])
                # 回溯
                self.path.pop()

        backtrack(0, 0)
        return self.res