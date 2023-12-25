import sys

N = int(sys.stdin.readline().strip())
coordinates = []

# 좌표 입력 받기
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinates.append([x, y])

def quickSort(lst, start, end):
    def partition(part, ps, pe):
        pivot = part[pe]
        i = ps - 1
        for j in range(ps, pe):
            # x좌표로 비교하고, x좌표가 같으면 y좌표로 비교
            if part[j][0] < pivot[0] or (part[j][0] == pivot[0] and part[j][1] < pivot[1]):
                i += 1
                part[i], part[j] = part[j], part[i]

        # pivot의 위치를 정해진 위치로 옮김
        part[i + 1], part[pe] = part[pe], part[i + 1]
        return i + 1

    if start < end:
        p = partition(lst, start, end)
        quickSort(lst, start, p - 1)
        quickSort(lst, p + 1, end)

quickSort(coordinates, 0, len(coordinates) - 1)

# 정렬된 좌표 출력
for i in range(len(coordinates)):
    print(f"{coordinates[i][0]} {coordinates[i][1]}")