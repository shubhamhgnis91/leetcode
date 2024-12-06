class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        bannedSet = set(banned)

        res = 0
        prefixSum = 0
        for i in range(1, n + 1):
            if i not in bannedSet:
                prefixSum += i
                if prefixSum <= maxSum:
                    res += 1

                else:
                    break

        return res