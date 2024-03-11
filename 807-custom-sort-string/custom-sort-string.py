class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        
        res = ""
        charMap = {}

        for letter in s:
            charMap[letter] = charMap.get(letter, 0) + 1

        for letter in order:
            if letter in charMap:
                res += charMap[letter] * letter
                charMap[letter] = 0
                        
        for letter in charMap:
            if charMap[letter] > 0:
                res += charMap[letter] * letter
        
        return res

        