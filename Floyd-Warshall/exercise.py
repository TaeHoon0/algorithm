import sys

INF = int(10e9)
V, E = map(int, sys.stdin.readline().split())
cities = [[INF] * (V + 1) for _ in range(V + 1)]
ans = INF

for i in range(1, V + 1):   # 자기 자신은 거리 0
    cities[i][i] = 0

for _ in range(E):  # 연결된 도로
    src, dst, distance = map(int, sys.stdin.readline().split())
    cities[src][dst] = distance

# k : k의 정점을 포함해 가는 경우
for k in range(1, V + 1):   # a->b 도로의 최소 길이 계산
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            cities[a][b] = min(cities[a][b], cities[a][k] + cities[k][b])

for i in range(1, V + 1):   # 사이클이 있는지 찾고, 길이 저장
    for j in range(1, V + 1):
        if i == j:
            continue
        if cities[i][j] != INF and cities[j][i] != INF:
            ans = min(ans, cities[i][j] + cities[j][i])

if ans != INF:
    print(ans)
else:
    print(-1)
