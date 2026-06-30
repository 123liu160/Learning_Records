# 给你一个二维数组 points，每个元素是一个坐标点 [x, y]。
# 还给你一个整数 k。
# 请返回 离原点 (0,0) 最近的 k 个点。
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 按 距离的平方 排序
        points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        # key表示按照什么元素来排序，lambda表示构建一个小函数，输入参数p输出距离原点的距离。
        # 取前 k 个，从0到k-1列表中的元素
        return points[:k]
# 第二种写法，用堆的方法实现。计算每个点到原点的距离
        # 把所有点放进堆里，堆会自动把最近的点放在最上面，取前 k 个就是答案
        # heap = []
        # for x, y in points:
        #     dist = x ** 2 + y ** 2
        #     将距离和对应的坐标存入堆中
        #     heapq.heappush(heap, (dist, x, y))
        # res = []
        # 取出前k个坐标
        # for _ in range(k):
        # 取堆
        #     dist, x, y = heapq.heappop(heap)
        #     res.append([x, y])
        #
        # return res