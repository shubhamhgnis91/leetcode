class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s = sorted(score, reverse=True)
        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i + 1) for i in range(3, len(s))]
        dt = dict(zip(s, medal))
        return [dt[i] for i in score]