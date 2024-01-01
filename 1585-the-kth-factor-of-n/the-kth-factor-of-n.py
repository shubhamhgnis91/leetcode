class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        inc = 1 if n % 2 == 0 else 2

        i=1
        count=0

        while i <= n:

            if n % i == 0:
                count+=1

                if count == k:
                    return i

            i += inc

        return -1
