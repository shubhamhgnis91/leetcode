class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        m = {}
        res = []

        for n in nums:
            m[n] = m.get(n, 0) + 1

        for num in m:
            if m[num] == 1:
                res.append(num)

            if len(res) == 2:
                return res
                

        
