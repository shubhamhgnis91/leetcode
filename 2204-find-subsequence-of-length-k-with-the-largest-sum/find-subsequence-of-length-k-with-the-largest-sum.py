class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        mp = collections.defaultdict(list)

        for i, num in enumerate(nums):
            mp[num].append(i)

        res = sorted(nums, reverse = True)[:k]

        selected = []
        for num in res:
            selected.append((mp[num].pop(0), num))

        selected.sort()

        res = []

        for _, num in selected:
            res.append(num)

        return res




        