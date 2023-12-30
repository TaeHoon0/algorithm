class Solution:
    def climbStairs(self, n: int) -> int:
        step = [0] * (n + 1)
        step[1] = 1

        if n > 1:
            step[2] = 2

        for i in range(1, n + 1):
            if i > 2:
                step[i] = step[i - 1] + step[i - 2]

        return step[n]