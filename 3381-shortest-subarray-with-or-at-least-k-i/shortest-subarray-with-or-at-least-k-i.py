class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        minLen = float('inf')
        
        for i in range(len(nums)):
            res = 0
            for j in range(i, len(nums)):
                res |= nums[j]
            
                if res >= k:
                    minLen = min(minLen, j - i + 1)              
        
        
        
        
        return -1 if minLen == float('inf') else minLen