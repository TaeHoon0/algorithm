class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        pre = intervals[0]

        for cur in range(1, len(intervals)):
            # 현재의 왼쪽 값이 이전의 최댓값보다 작을 때 큰 값 비교해서 넣기
            if intervals[cur][0] <= pre[1]:
                pre[1] = max(pre[1], intervals[cur][1])
            else:
                ans.append(pre)
                pre = intervals[cur]
        ans.append(pre)
        return ans