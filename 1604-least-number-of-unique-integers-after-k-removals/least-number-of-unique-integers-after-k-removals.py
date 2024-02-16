class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

        d = {}

        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        elements = sorted(d.items(), key=lambda x:x[1])

        for key, value in elements:
            if value <= k:
                k -= value
                del d[key]
            
            else:
                break

        return len(d)