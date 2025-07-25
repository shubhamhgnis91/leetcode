class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num > 0:
                s.add(num)

        return sum(s) if len(s) > 0 else sorted(nums)[-1]