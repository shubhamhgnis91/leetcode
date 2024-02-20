class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numbers = {}
        res = -1
        
        for num in nums:
            numbers[num] = numbers.get(num , 0) + 1
        
        for i in range(len(nums) + 1):
            if i not in numbers:
                res = i
                break
        
        return res