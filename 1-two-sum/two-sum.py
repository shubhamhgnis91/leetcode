class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if nums[i] in dMap:
                return [dMap[nums[i]], i]
            else:
                dMap[diff] = i
        
            

