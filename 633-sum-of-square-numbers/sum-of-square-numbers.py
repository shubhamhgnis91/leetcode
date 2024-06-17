class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left = 0
        right = int(c ** 0.5)

        while left <= right:
            temp = left * left + right * right
            if temp == c:
                return True

            if temp < c:
                left += 1

            else:
                right -= 1

        return False