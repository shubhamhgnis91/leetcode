class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
        m=len(mat)
        n=len(mat[0])
        row=[0] * m
        cols=[0] * n
        res=0

        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    row[i]+=1
                    cols[j]+=1

        for i in range(m):
            for j in range(n):
                if mat[i][j]==1 and row[i]==1 and cols[j]==1:
                    res+=1

        return res