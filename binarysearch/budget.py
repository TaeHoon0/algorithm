import sys

N = int(sys.stdin.readline().strip())
budgets = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())

def binarySearch(arr, start, end):
    result = 0

    while start <= end:
        mid = (start + end) // 2    # 상한액
        total = 0

        for budget in arr:
            total += min(budget, mid)

        if total <= M:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result

print(binarySearch(budgets, 0, max(budgets)))
