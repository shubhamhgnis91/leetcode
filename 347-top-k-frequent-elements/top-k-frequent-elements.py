class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mp = {}

        for num in nums:
            mp[num] = mp.get(num, 0) + 1

        mp = dict(sorted(mp.items(), key = lambda x:x[1], reverse = True))
        res = []
        for item in mp:
            if k < 1:
                break

            res.append(item)
            k -= 1

        return res
