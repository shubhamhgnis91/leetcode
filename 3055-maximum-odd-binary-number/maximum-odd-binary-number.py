class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        res = ""        

        oneBits = s.count('1')
        zeroBits = len(s) - oneBits

        res += '1' * (oneBits - 1)
        res += '0' * (zeroBits)
        res += '1'

        return res

