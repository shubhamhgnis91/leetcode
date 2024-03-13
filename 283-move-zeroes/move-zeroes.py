class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        p = q = 0

        while p < len(nums) and q < len(nums):
            
            if nums[p] != 0 and nums[q] == 0:
                nums[p], nums[q] = nums[q], nums[p]

            if nums[q] != 0:
                q += 1

            p += 1