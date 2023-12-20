import sys

T = int(sys.stdin.readline().strip())
nums = [1, 2, 3]

for _ in range(T):
    n = int(sys.stdin.readline().strip())

    def dfs(cur_sum, cnt):
        if cur_sum == n:
            cnt += 1
            return cnt

        if cur_sum > n:     #가지치기
            return cnt

        for num in nums:
            cnt = dfs(cur_sum + num, cnt)

        return cnt

    print(dfs(0,0))