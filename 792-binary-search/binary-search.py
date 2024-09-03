class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binSearch(arr, left, right, key):

            if left > right:
                return -1

            mid = left + (right - left) // 2

            if arr[mid] == key:
                return mid

            if arr[mid] > key:
                return binSearch(arr, left, mid - 1, key)

            return binSearch(arr, mid + 1, right, key)

        
        return binSearch(nums, 0, len(nums) - 1, target)