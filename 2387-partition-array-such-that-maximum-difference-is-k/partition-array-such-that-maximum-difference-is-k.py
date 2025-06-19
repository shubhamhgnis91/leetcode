class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        count = 1

        minN = nums[0]
        maxN = nums[0] + k

        for i in range(1, len(nums)):
            if nums[i] > maxN:
                minN = nums[i]
                maxN = nums[i] + k
                count += 1
        
        return count





