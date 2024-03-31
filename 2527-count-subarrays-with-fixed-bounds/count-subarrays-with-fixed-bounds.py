class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        res = 0
        prevMin = prevMax = -1
        j = -1

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                j = i

            if nums[i] == minK:
                prevMin = i

            if nums[i] == maxK:
                prevMax = i

            res += max(0, min(prevMin, prevMax) - j)

        
        return res