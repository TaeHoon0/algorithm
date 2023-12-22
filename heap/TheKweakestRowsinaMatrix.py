import heapq
from heapq import heappush

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        ans = []

        for row in range(len(mat)):
            cnt = 0
            for column in mat[row]:
                if column == 1:
                    cnt += 1
            heappush(heap, [cnt, row])

        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans