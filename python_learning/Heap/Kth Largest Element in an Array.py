# 给你一个无序数组 nums 和整数 k。
# 返回数组中 第 k 大的数。
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            # 保持堆的大小最多为 k
            if len(heap) > k:
                heapq.heappop(heap)
        # 堆顶就是第 k 大
        return heap[0]