class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = max(nums)  # 배열에서 가장 큰 값을 초기 결과로 설정
        if result <= 0:
            return result  # 만약 배열의 모든 값이 음수이면 가장 큰 값이 최대 부분 배열 합이 됨

        sum = 0
        for i in nums:
            sum = max(sum + i, 0)  # 현재까지의 합이 음수이면 버리고 새로운 시작으로 갱신
            result = max(sum, result)  # 최대 부분 배열 합 갱신

        return result