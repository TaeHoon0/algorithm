class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def check_swap(a, b):
            return str(a) + str(b) < str(b) + str(a) # 스왑 한 경우가 더 큰 경우 (True 반환)

        i = 1
        while i < len(nums):
            j = i
            while j > 0 and check_swap(nums[j - 1], nums[j]):
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
            i += 1
        return str(int(''.join(map(str,nums))))