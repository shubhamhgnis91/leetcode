class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set()
        maxim = nums[0]
        res = 0
        for i in range(len(nums)):
            if nums[i] > maxim:
                maxim = nums[i]
            
            if nums[i] > 0 and nums[i] not in s:
                res += nums[i]
                s.add(nums[i])

        return maxim if maxim < 0 else res
        