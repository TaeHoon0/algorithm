import sys
from collections import defaultdict

INF = int(10e9)
N, M, C = map(int, sys.stdin.readline().split())
cities = [[INF] * (N + 1) for _ in range(N + 1)]
cnt = 0
max_time = 0

for _ in range(M):
    X, Y, Z = map(int, sys.stdin.readline().split())    # X로부터 Y에 메시지 시간 Z
    cities[X][Y] = Z

for i in range(1, N + 1):   # 자기 자신의 값 0
    cities[i][i] = 0

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            cities[a][b] = min(cities[a][b], cities[a][k] + cities[k][b])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if cities[i][j] != 0 and cities[i][j] != INF:
            cnt += 1
            max_time = max(max_time, cities[i][j])

print(cnt, max_time)