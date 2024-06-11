class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        d = [0] * 1001
        res = []

        for n in arr1:
            d[n] += 1

        for i in range(len(arr2)):
            while d[arr2[i]] > 0:
                res.append(arr2[i])
                d[arr2[i]] -= 1

        for i in range(len(d)):
            while d[i] > 0:
                res.append(i)
                d[i] -= 1

        return res
        
