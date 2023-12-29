import sys
import heapq

cnt = 0
while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break

    visited = [[10000] * N for _ in range(N)]
    cave = [[] for _ in range(N)]
    dx = [1, 0, -1, 0]  # 좌우
    dy = [0, 1, 0, -1]  # 상하

    for i in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        cave[i] = row

    q = []
    visited[0][0] = cave[0][0]

    heapq.heappush(q, (cave[0][0], 0, 0)) # 시작 위치

    while q:
        acc, r, c = heapq.heappop(q)    #누적 루피, row, col

        # 방문할 필요 X
        if visited[r][c] < acc:
            continue

        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < N and 0 <= nc < N:
                rupee = acc + cave[nr][nc]
                if rupee < visited[nr][nc]:
                    visited[nr][nc] = rupee
                    heapq.heappush(q, (rupee, nr, nc))

    cnt += 1
    print(f"Problem {cnt}: {visited[N - 1][N - 1]}")
