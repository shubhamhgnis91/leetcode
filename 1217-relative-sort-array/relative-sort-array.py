class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        d = {}
        res = []
        temp = []


        for n in arr1:
            d[n] = d.get(n, 0) + 1

        for i in range(len(arr2)):
            while d[arr2[i]] > 0:
                res.append(arr2[i])
                d[arr2[i]] -= 1

        for n in d:
            while d[n] > 0:
                temp.append(n)
                d[n] -= 1

        return res + sorted(temp)
        
