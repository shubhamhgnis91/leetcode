class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        
        min1=float('inf')
        min2=float('inf')

        for i in range(len(prices)):
            
            if prices[i]<min1:
                min2=min1
                min1=prices[i]                

            elif prices[i]<min2:
                min2=prices[i]
            
        return money if (min1+min2) > money else (money-(min1+min2))  