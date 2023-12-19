class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m=len(img)
        n=len(img[0])

        res=[]

        for i in range(m):
            row=[]            
            for j in range(n):
                s=0
                count=0                
                for x in range(max(0,i-1),min(m,i+2)):
                    for y in range(max(0,j-1),min(n,j+2)):
                        s+=img[x][y]
                        count+=1
                row.append(int(s/count))
            res.append(row)
        
        return res