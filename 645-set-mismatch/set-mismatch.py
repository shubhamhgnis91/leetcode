class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        res =[]

        for num in nums:
            if num in d:
                res.append(num)
                d[num] += 1
            else:
                d[num] = 1
        
        for i in range(1,(len(nums) + 1)):
            if i not in d:
                res.append(i)
        
        return res
        