class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mp = {}

        for num in nums:
            mp[num] = mp.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for item in mp:
            bucket[mp[item]].append(item)

        res = []

        for i in range(len(bucket) - 1, -1, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
