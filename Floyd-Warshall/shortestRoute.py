import sys

INF = int(10e9)
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline().strip())

edge = [[INF] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())  # 출발점, 도착점, 가중치
    edge[u][v] = w

for i in range(1, V + 1):
    edge[i][i] = 0

for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            edge[i][j] = min(edge[i][j], edge[i][k] + edge[k][j])

for i in range(1, V + 1):
    if i == K:
        for j in range(1, V + 1):
            if edge[i][j] != INF:
                print(edge[i][j])
            else:
                print("INF")
        break
