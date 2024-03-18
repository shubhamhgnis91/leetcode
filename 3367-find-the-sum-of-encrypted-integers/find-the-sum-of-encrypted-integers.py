class Solution(object):
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = 0
        
        for i in range(len(nums)):
            n = str(nums[i])          
            res += int(len(n) * max(n))
            
        return res
            
            
            
            