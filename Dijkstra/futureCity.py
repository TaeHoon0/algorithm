import sys
import heapq

def city(graph, start, destination):
    N = len(graph)
    INF = 1000000
    dist = [INF for _ in range(N + 1)]
    q = []
    distance = 0

    dist[start] = 0     # 시작점 거리 0
    heapq.heappush(q, (0, start))    # 큐에 코스트, 시작 위치 넣기

    # 목표에 도착할 때까지
    while q:
        acc, cur = heapq.heappop(q)     # 현재 코스트의 합, 현재 위치

        if cur == destination:    # 목표에에 도착하면, 현재까지 코스트 반환
            distance = acc
            break

        # 현재 코스트의 합보다, 해당 노드를 들렸을 때 드는 코스트가 더 크면 할 필요x
        if dist[cur] < acc:
            continue

        for adj in graph[cur]:
            cost = acc + 1              # 거리당 코스트 1
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    if dist[destination] == INF:        # 도착하지 못 한 경우
        return -1

    return distance

# 회사의 개수, 간선의 개수
N, M = map(int, sys.stdin.readline().split())
edges = {key: [] for key in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)

# K 들리고, X 회사에 도착
X, K = map(int, sys.stdin.readline().split())

if city(edges, 1, K) == -1 or city(edges, K, X) == -1:
    print(-1)
else:
    print(city(edges, 1, K) + city(edges, K, X))
