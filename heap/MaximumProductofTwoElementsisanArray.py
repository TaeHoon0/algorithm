import heapq
from heapq import heappush

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        
        for num in nums:
            heappush(heap, -num)

        max_first = -heapq.heappop(heap)
        max_second = -heapq.heappop(heap)

        return (max_first - 1) * (max_second - 1)
