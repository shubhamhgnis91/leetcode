class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hmap = {}
        for num in arr : 
            if num in hmap : 
                hmap[num] += 1
            else:
                hmap[num] = 1
        
        return len(hmap) == len(set(hmap.values()))
