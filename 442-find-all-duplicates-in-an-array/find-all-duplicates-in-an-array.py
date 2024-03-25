class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        res = []

        for num in nums:
            x = abs(num) - 1
            if nums[x] < 0:
                res.append(x + 1)
            
            else:
                nums[x] *= -1

        return res

        