class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        def fibo(n, dp):

            if n <= 1:
                return n

            if dp[n] != -1:
                return dp[n]

            dp[n] = fibo(n-1, dp) + fibo(n-2, dp)

            return dp[n]
        
        dp = [-1] * (n + 1)

        return fibo(n, dp)
