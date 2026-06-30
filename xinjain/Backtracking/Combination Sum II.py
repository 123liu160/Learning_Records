# 你有一个整数数组 candidates（可能包含重复数字）和一个目标整数 target。你的任务是返回所有唯一的组合列表，使得选中的数字之和等于 target。
# 数组中的每个元素最多只能被选中一次。
# 返回的解集不能包含重复的组合。
# 你可以按任意顺序返回组合，每个组合内部的数字顺序也不作要求。
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        # 排序
        candidates.sort()

        def backtrack(start, cur_sum):
            # 终止条件：和等于目标值
            if cur_sum == target:
                res.append(path.copy())
                return
            # 和超过目标，直接返回
            if cur_sum > target:
                return

            for i in range(start, len(candidates)):
                # 核心去重：同一层跳过相同数字，避免重复组合
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # 选择当前元素
                path.append(candidates[i])
                # 每个元素只能选一次，下一轮从 i+1 开始
                backtrack(i + 1, cur_sum + candidates[i])
                # 回溯，撤销选择
                path.pop()

        backtrack(0, 0)
        return res