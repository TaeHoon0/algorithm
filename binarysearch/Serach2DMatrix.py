class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        result = False

        def binarySearch(arr, target, start, end):
            while start <= end:
                mid = (start + end) // 2
                print(arr[mid])
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return False

        for m in matrix:
            result = binarySearch(m, target, 0, len(m) - 1)
            if result:
                break

        return result
