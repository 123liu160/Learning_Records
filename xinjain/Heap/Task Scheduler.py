# 给你一堆 CPU 任务（比如 A A A B B B），还有一个冷却时间 n。
# 规则：
# 同一个任务 必须间隔 至少 n 个周期 才能再次执行
# 每个周期只能做一个任务
# 问：最少需要多少个周期才能做完所有任务？
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 统计每个任务出现几次
        count = Counter(tasks)
        # 找到【最大次数】
        max_count = max(count.values())
        # 找到【有多少个任务达到最大次数】
        max_num = list(count.values()).count(max_count)
        # 套公式
        res = (max_count - 1) * (n + 1) + max_num
        # 最后答案不能比任务总数小
        return max(res, len(tasks))
    #如果任务为【A, A, A, B, B, B】
    # A → B → 空闲 → A → B → 空闲 → A → B
    # 1   2    3    4   5    6    7   8
    #公式 = (最多次数 - 1) × (n + 1) + 达到最多次数的任务数量
    # 公式算出来的是有强制冷却、存在空闲位的最小长度。
    # 但有一种情况：任务数量极多，冷却约束被 “填满”，没有空闲位。
    # 例如任务为【A, A, B, B, C, C, D】公式计算出为5，小于任务数量，所以正确结果应该是任务数7