class Solution:
    def specialArray(self, nums: List[int]) -> int:
        

        def count(n: int, nums: List[int]) -> int:
            
            ans = 0
            for num in nums:
                if num >= n:
                    ans += 1

            return ans


        for x in range(len(nums) + 1):
            ans = count(x, nums)

            if x == ans:
                return ans

        return -1