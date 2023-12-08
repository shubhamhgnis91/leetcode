class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        

        i=len(num)-1
        while i >= 0:

          if int(num[i]) % 2 != 0:
            return num

          num = num[:-1]
          i=i-1
          
        return num  
        