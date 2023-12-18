class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        tMatrix=[]

        r=len(matrix)
        c=len(matrix[0])

        for j in range(c):
            temp=[]
            for i in range(r):
                temp.append(matrix[i][j])
            tMatrix.append(temp)
        return tMatrix