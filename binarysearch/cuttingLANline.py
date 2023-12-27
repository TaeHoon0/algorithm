import sys

K, N = map(int, sys.stdin.readline().split())

lines = []

for _ in range(K):
    lines.append(int(sys.stdin.readline().strip()))

def binarySearch(arr, start, end):
    result = 0

    while start <= end:
        mid = (start + end) // 2
        total = 0

        for line in arr:
            if mid > 0:
                total += line // mid

        if total >= N:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result

print(binarySearch(lines, 1, max(lines)))
