class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        negCount = 0
        ans = 0
        s = 10e5 + 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] < 0:
                    negCount += 1

                ans += abs(matrix[i][j])
                s = min(s, abs(matrix[i][j]))

        if negCount % 2 == 0:
            return ans

        ans -= 2 * s

        return ans
