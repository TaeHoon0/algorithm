import heapq
from heapq import heappush

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []
        ans = 0

        for num in nums:
            heappush(heap, -num)

        for _ in range(k):
            ans = -heapq.heappop(heap)

        return ans