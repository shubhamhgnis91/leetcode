class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        m = {}
        for num in banned:
            m[num] = m.get(num, 0) + 1

        res = 0
        prefixSum = 0
        for i in range(1, n + 1):
            if i not in banned:
                prefixSum += i
                if prefixSum <= maxSum:
                    res += 1

                else:
                    break
        
        return res