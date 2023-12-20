import sys

N = int(sys.stdin.readline())
block = []
apart = []
count = 0
x = [1, -1, 0, 0] # 좌우
y = [0, 0, 1, -1] # 상하

for i in range(N):
    block.append(list(map(int, sys.stdin.readline().rstrip())))


def dfs(r, c):  # 1일 때 호출
    # 범위 밖이거나, 단지가 아닌경우
    if r < 0 or r >= N or c < 0 or c >= N or block[r][c] == 0:
        return
    block[r][c] = 0                      # 탐색완료

    for i in range(4):
        dfs(r + x[i], c + y[i])            # 상하좌우로 움직이면서 검색

    apart[-1] += 1
    return


for r in range(N):      # row
    for c in range(N):  # column
        node = block[r][c]
        if node != 1:
            continue
        # 1을 만나게 되면 주변 탐색
        apart.append(0)
        dfs(r, c)

print(len(apart))
for i in range(len(apart)):
    print(apart[i])