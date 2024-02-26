class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        trib = [0, 1, 1]

        for i in range(3, n + 1):
            trib.append(trib[i - 1] + trib[i - 2] + trib[i - 3])

        return trib[n]