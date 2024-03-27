class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        count = 0        
        l = 0
        r = 0
        prod = 1

        while r < len(nums):
            prod *= nums[r]

            while l <= r and prod >= k:
                prod /= nums[l]
                l += 1

            count += (r - l + 1)
            r += 1
        
        return count
                