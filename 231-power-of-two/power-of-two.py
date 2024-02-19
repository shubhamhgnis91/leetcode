class Solution(object):
    def isPowerOfTwo(self, n):
        if n<=0: return False
        x=math.log(n)/log(2)
        return True if x-math.trunc(x)<0.000000001 else False