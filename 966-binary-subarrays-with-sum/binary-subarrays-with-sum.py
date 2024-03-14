class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        s = 0
        p = {0:1}
        res = 0

        for num in nums:
            s += num
            res += p.get(s-goal, 0)
            p[s] = p.get(s, 0) + 1

        return res
