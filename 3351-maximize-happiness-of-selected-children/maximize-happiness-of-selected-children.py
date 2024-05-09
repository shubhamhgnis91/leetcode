class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        selected = happiness[:k]

        for i in range(k):
            if selected[i] > 0:
                selected[i] = max(selected[i] - i, 0)
                res += selected[i]
        
        return res