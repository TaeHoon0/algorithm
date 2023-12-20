from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)   #list형태로 dictionary 생성

        #정렬해서 입력
        for src, dst in sorted(tickets):
            graph[src].append(dst)

        route = []
        def dfs(src):
            #첫번째 값을 읽어서 어휘순으로 방문, 중복된 곳을 방문할 수도 있기 때문에
            #visited 검사할 필요x
            while graph[src]:
                dfs(graph[src].pop(0))
            route.append(src)

        dfs("JFK")
        #stack의 형태이기 때문에 역순 반환
        return route[::-1]