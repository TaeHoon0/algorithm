import heapq
import sys
from heapq import heappush

N = int(sys.stdin.readline().strip())
heap = []

for _ in range(N):
    temp = sys.stdin.readline().strip().split(" ")
    time = int(temp[0]) * 10000 + int(temp[1]) * 100 + int(temp[2])
    heappush(heap, time)

for _ in range(N):
    time = heapq.heappop(heap)
    print(f"{time // 10000} {(time // 100) % 100} {time % 100}")
