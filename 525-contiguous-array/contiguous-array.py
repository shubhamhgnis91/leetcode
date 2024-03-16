class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        m = {0:0}
        count = 0

        res = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1

            else:
                count += 1

            if count in m:
                res = max(res, (i + 1) - m[count])

            else:
                m[count] = (i + 1)

        return res