import sys

N = int(sys.stdin.readline().strip())
coordinates = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinates.append([x, y])

def quickSort(lst, start, end):
    def partition(part, ps, pe):
        pivot = part[pe]
        i = ps - 1
        for j in range(ps, pe):             # j는 현재 바라보고 있는 위치
            if part[j][0] < pivot[0]:       # pivot의 값보다 작거나 같으면 배열의 시작위치부터 넣는다.
                i += 1
                part[i], part[j] = part[j], part[i]
            if part[j][0] == pivot[0]:      # x좌표의 값이 같을 때
                if part[j][1] < pivot[1]:
                    part[i], part[j] = part[j], part[i]

        # pivot의 위치를 pivot보다 작거나 같았던 값들 바로 뒤로 옮김
        part[i + 1], part[pe] = part[pe], part[i + 1]

        return i + 1

    if start >= end:
        return

    p = partition(lst, start, end)
    quickSort(lst, start, p - 1)
    quickSort(lst, p + 1, end)

    return lst

quickSort(coordinates, 0, len(coordinates) - 1)

for i in range(len(coordinates)):
    print(f"{coordinates[i][0]} {coordinates[i][1]}")