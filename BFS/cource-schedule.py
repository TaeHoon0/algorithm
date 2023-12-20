import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        #그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()      #이미 방문한 노드
        visited = set()     #모든 탐색이 끝난 후에 노드를 추가
                            #탐색 도중 순환 구조가 발견된다면, false이며 visited에 추가x

        def dfs(i):
            #순환 구조
            if i in traced:
                return False
            #이미 방문한 노드
            if i in visited:
                return True

            traced.add(i)

            for y in graph[i]:
                if not dfs(y):
                    return False

            #탐색 종료 후, 순환 노드 삭제
            traced.remove(i)
            #순환 구조x, 방문한 노드x이므로 방문 노드에 추가
            visited.add(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True

