import heapq
import sys
from heapq import heappush

N = int(sys.stdin.readline().strip())
heap = []
# x > 0 배열 추가, 0가장 작은 값 출력
for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x > 0:
        heappush(heap, x)
    if x == 0:
        if len(heap) == 0:
            print(0)
            continue
        print(heapq.heappop(heap))

