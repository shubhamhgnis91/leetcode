class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        return '1' * (s.count('1') - 1) + '0' * (s.count('0')) + '1'

