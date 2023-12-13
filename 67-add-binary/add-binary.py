class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res=lambda a,b : bin(int(a,2) + int(b,2))
        return res(a,b)[2:]