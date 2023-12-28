class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        # 현재 노드, 연결된 노드, 걸리는 시간
        for x, y, w in times:
            adj_list[x].append((w, y))

        visited = set()
        q = [(0, k)]
        while q:
            travel_time, node = heapq.heappop(q)
            visited.add(node)

            if len(visited) == n:
                return travel_time

            for time, adj in adj_list[node]:
                if adj not in visited:
                    q.heappush(q, (travel_time + time, adj))

        return -1