import sys

while True:
    N = int(sys.stdin.readline().rstrip())

    if N == 0:
        break

    cards = [x for x in range(1, 51)]
    start = 1
    end = 50
    ans = []
    while start <= end:
        mid = (start + end) // 2
        ans.append(str(mid))

        if mid == N:
            print(' '.join(ans))
            break
        elif mid < N:
            start = mid + 1
        else:
            end = mid - 1
