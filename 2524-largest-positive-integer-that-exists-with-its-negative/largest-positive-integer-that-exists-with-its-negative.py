class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)

        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[j] == -nums[i]:
                return nums[i]

            elif nums[i] > -nums[j]:
                i += 1

            else:
                j -= 1

        return -1
