class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = {}
        for i, num in enumerate(nums):
            mp[num] = i

        for i, num in enumerate(nums):
            if (target - num) in mp and mp[target - num] != i:
                return [i, mp[target - num]]