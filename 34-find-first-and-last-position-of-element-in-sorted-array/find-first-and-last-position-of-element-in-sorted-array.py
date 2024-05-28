class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        res = [-1, -1]

        l = 0
        r = len(nums) - 1

        while l <= r:

            m = (l + r) // 2

            if target == nums[m]:
                res[0] = m
                r = m - 1

            elif target > nums[m]:
                l = m + 1

            else:
                r = m - 1

        l = 0
        r = len(nums) - 1

        while l <= r:

            m = (l + r) // 2

            if target == nums[m]:
                res[1] = m
                l = m + 1

            elif target > nums[m]:
                l = m + 1

            else:
                r = m - 1


        return res



        

