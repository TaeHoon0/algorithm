class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def binarySearch(arr, num, start, end):
            while start <= end:
                mid = (start + end) // 2

                if num + arr[mid] == target:
                    return mid
                elif num + arr[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return None

        for idx1 in range(len(numbers)):
            idx2 = binarySearch(numbers, numbers[idx1], idx1 + 1, len(numbers) - 1)  # idx1 + 1부터 검사
            if idx2 is not None and idx1 != idx2:
                return [idx1 + 1, idx2 + 1]  # 인덱스가 0부터 시작이 아닌 1부터 시작



