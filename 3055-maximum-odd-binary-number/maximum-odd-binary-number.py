class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        res = ""
        bitFreq = {}

        for bit in s:
            bitFreq[bit] = bitFreq.get(bit, 0) + 1
        
        if '0' not in bitFreq:
            return s

        oneBits = bitFreq['1']
        zeroBits = bitFreq['0']

        while oneBits > 1:
            res += '1'
            oneBits -= 1
        
        while zeroBits:
            res += '0'
            zeroBits -= 1

        res += '1'

        return res

