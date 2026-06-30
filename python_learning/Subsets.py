# 输入：一个元素不重复的数组 nums
# 输出：所有可能的子集（包括空集、全集）
# 要求：子集不重复，顺序不限
class Solution:
    # 定义函数：输入是数字列表，输出是子集的列表
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 1. 存放最终所有子集的总仓库
        self.res = []

        # 2. 存放当前正在拼的子集（会不断变化）
        self.path = []

        # 3. 定义回溯函数：start 表示从第几个数字开始选
        def backtrack(start):
            # 4.每一步的 path 都是一个合法子集，直接存起来
            # 必须用 copy()，否则存的是地址，后面会变空
            self.res.append(self.path.copy())

            # 5. 循环：从 start 开始遍历所有数字
            # 作用：保证不回头选，避免 [1,2] 和 [2,1] 重复
            for i in range(start, len(nums)):
                # 6. 做选择：把当前数字放进子集里
                self.path.append(nums[i])

                # 7. 递归：继续往下选，下一次只能从 i+1 开始
                backtrack(i + 1)

                # 8. 回溯：撤销刚才的选择，删掉最后一个数字
                self.path.pop()

        # 9. 启动回溯，从第 0 个数字开始选
        backtrack(0)

        # 10. 返回所有子集
        return self.res