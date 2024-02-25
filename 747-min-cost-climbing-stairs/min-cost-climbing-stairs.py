class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        def solve(cost, n, dp):
            if n <= 1:
                return cost[n]
            
            if dp[n] != -1:
                return dp[n]

            dp[n] = cost[n] +  min(solve(cost, n - 1, dp), solve(cost, n -2, dp))
            return dp[n]   
        
        n = len(cost)
        dp = [-1] * (n + 1)
        ans = min(solve(cost, n - 1, dp), solve(cost, n - 2, dp))
        return ans