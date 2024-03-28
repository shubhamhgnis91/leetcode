class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        res = 0
        freq = {}
        n = len(nums)
        left = 0

        for right in range(n):
            curr = nums[right]
            freq[curr] = freq.get(curr, 0) + 1

            while left <= right and freq[curr] > k:
                freq[nums[left]] = freq.get(nums[left], 0) - 1
                left += 1

            res = max(res, right - left + 1)
        
        return res
            

            
