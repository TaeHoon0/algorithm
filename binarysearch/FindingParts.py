import sys

N = int(sys.stdin.readline().strip())
parts = list(map(int,  sys.stdin.readline().split()))
parts.sort()

M = int(sys.stdin.readline().strip())
requirements = list(map(int,  sys.stdin.readline().split()))

#정렬 후, 가운데를 기준으로 값을 찾음
def binarySearch(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            end = mid + 1
    return False

for r in requirements:
    result = binarySearch(parts, r, 0, N - 1)
    if result:
        print('yes', end=' ')
    else:
        print('no', end=' ')