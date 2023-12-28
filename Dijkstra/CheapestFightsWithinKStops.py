import heapq
from collections import defaultdict


class Solution:
    # n : 정거장 수, filghts: [출발지, 목적지, 가격], src: 출발지, dst: 목적지, k: 최대 경유하는 정거장
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj_list = defaultdict(list)
        q = []
        min_price = int(10e7)

        # 출발지, 도착지, 가격
        for start, end, price in flights:
            adj_list[start].append((price, end))

        visited = set()
        heapq.heappush(q, (0, src, 0))  # 비용, 출발지, 경유한 수

        while q:
            acc, cur, cur_cnt = heapq.heappop(q)   # 누적금액, 현재위치, 경유 수

            if (cur, cur_cnt) in visited:          # 이미 들린 곳이라면 pass
                continue

            visited.add((cur, cur_cnt))

            if cur == dst:                         # 가장 작은 가격 찾기
                min_price = min(acc, min_price)

            if cur_cnt <= k:                       # 경유지가 k와 같거나 낮을 때까지 탐색
                for price, adj in adj_list[cur]:
                    heapq.heappush(q, (acc + price, adj, cur_cnt + 1))

        if min_price == int(10e7):                 # 최소가격이 변하지 않았다면 도착 x
            return -1
        else:
            return min_price
