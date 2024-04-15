class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        
        num = str(x)
        temp = 0
        
        for digit in num:
            temp += int(digit)
            
        return temp if x % temp == 0 else -1