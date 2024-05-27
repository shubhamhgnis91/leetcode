class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        nums.sort()

        def count(n: int, nums: List[int]) -> int:
            
            ans = 0
            for num in nums:
                if num >= n:
                    ans += 1

            return ans


        l = 0
        r = len(nums)

        while l <= r:
            m = (l + r) // 2

            ans = count(m, nums)

            if m == ans:
                return m

            if ans > m:
                l = m + 1

            else:
                r = m - 1

        return -1