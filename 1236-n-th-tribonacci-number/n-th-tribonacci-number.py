class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        
        if n == 2:
            return 1
        
        trib = [-1] * (n + 1)
        trib[0] = 0
        trib[1] = 1
        trib[2] = 1

        for i in range(3, n + 1):
            trib[i] = trib[i - 1] + trib[i - 2] + trib[i - 3]

        return trib[n]