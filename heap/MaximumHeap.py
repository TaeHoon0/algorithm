import heapq
import sys
from heapq import *

N = int(sys.stdin.readline().strip())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x > 0:
        heappush(heap, -x)
    if x == 0:
        if len(heap) == 0:
            print(0)
            continue
        print(-heapq.heappop(heap))