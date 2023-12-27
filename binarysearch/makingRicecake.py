import sys

N, M = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))

def binarySearch(arr, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0

        # 떡을 잘랐을 때의 남은 양의 합을 계산
        for x in arr:
            if x > mid:
                total += x - mid

        # 요청한 길이보다 작을 때, 더 많이 자르기
        if total < M:
            end = mid - 1
        else:
            result = mid    # 반복해 나가면서 mid값을 최대한 적게 잘랐을 때까지 찾음
            start = mid + 1

    return result

print(binarySearch(heights, 0, max(heights)))
