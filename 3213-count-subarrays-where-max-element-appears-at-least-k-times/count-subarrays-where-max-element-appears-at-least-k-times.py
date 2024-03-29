class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        n = len(nums)
        res = 0
        count = 0
        left = 0
        right = 0

        while right < n:
            if nums[right] == m:
                count += 1

            while count >= k:
                if nums[left] == m:
                    count -= 1
                    
                left += 1
            
            res += left

            right += 1

        return res

