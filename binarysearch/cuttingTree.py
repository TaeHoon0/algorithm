import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

def binarySearch(arr, start, end):
    height = 0

    while start <= end:
        mid = (start + end) // 2
        total = 0 # 가져가는 나무의 합

        for x in trees:
            if x > mid:
                total += x - mid

        if total >= M:
            start = mid + 1
            height = mid
        else:
            end = mid - 1

    return height

print(binarySearch(trees, 0, max(trees)))
