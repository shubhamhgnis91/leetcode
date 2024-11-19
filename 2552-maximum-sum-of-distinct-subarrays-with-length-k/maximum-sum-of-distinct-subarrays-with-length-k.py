class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        s = 0
        mp = {}

        for i in range(len(nums)):
            s += nums[i]
            mp[nums[i]] = mp.get(nums[i], 0) + 1

            if i >= k - 1:
                if len(mp) == k:
                    res = max(res, s)
                
                s -= nums[i - k + 1]
                mp[nums[i - k + 1]] -= 1

                if mp[nums[i - k + 1]] == 0:
                    mp.pop(nums[i - k + 1])

        return res