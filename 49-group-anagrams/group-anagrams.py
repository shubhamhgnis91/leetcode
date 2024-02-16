class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        dictionary = {}
        res = []

        for i in range(len(strs)):
            temp = tuple(sorted(strs[i]))
            
            if temp in dictionary:
                dictionary[temp].append(strs[i])
            
            else:
                dictionary[temp] = [strs[i]]

        for i in dictionary:
            res.append(dictionary[i])

        return res