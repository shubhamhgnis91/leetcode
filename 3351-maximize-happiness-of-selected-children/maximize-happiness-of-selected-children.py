class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0

        for i in range(k):
            if happiness[i] > 0:
                happiness[i] = max(happiness[i] - i, 0)
                res += happiness[i]
        
        return res