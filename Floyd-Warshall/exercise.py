import sys

INF = int(10e9)
V, E = map(int, sys.stdin.readline().split())
cities = [[INF] * (V + 1) for _ in range(V + 1)]
ans = INF

for _ in range(E):
    src, dst, distance = map(int, sys.stdin.readline().split())
    cities[src][dst] = distance

for i in range(1, V + 1):
    cities[i][i] = 0

# k : k의 정점을 포함해 가는 경우
for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            cities[a][b] = min(cities[a][b], cities[a][k] + cities[k][b])

for i in range(1, V + 1):
    for j in range(1, V + 1):
        if i == j:
            continue
        if cities[i][j] != INF and cities[j][i] != INF:
            ans = min(ans, cities[i][j] + cities[j][i])

if ans != INF:
    print(ans)
else:
    print(-1)
