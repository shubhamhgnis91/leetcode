class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 != 0:
            return False

        s//=2
        dp = []
        n = len(nums)

        for i in range(n + 1):
            row = []
            for j in range(s + 1):
                if j == 0:
                    row.append(True)
                else:
                    row.append(False)

            dp.append(row)

        for i in range(1, n + 1):
            for j in range(1, s + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = (dp[i - 1][j - nums[i - 1]]) or (dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][s]
