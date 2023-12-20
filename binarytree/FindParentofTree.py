#백준 11725
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline().strip())
edge = [[] for _ in range(N + 1)]
parent = [0] * (N+1)

for _ in range(N - 1):
    node_a, node_b = map(int, sys.stdin.readline().strip().split())
    edge[node_a].append(node_b)
    edge[node_b].append(node_a)

def dfs(node):    #edge, node, parent
    for i in edge[node]:        # 연결되어 있으면
        if not parent[i]:       # 부모노드가 없다면
            parent[i] = node
            dfs(i)

dfs(1)

for i in range(2, N + 1):
    print(parent[i])