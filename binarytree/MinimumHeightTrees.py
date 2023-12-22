from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        link = [[] for _ in range(n)]
        in_degree = [0] * n  # 각 노드의 간선의 수
        leaves = deque()

        # 양방향 연결 및 간선의 수
        for node_a, node_b in edges:
            link[node_a].append(node_b)
            link[node_b].append(node_a)
            in_degree[node_a] += 1
            in_degree[node_b] += 1

        # 간선의 수가 1인 리프 노드 초기화
        for i in range(n):
            if in_degree[i] == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            next_leaves_layer = deque()

            while leaves:
                leaf = leaves.popleft()
                for neighbor in link[leaf]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 1:
                        next_leaves_layer.append(neighbor)

            leaves = next_leaves_layer

        return list(leaves)