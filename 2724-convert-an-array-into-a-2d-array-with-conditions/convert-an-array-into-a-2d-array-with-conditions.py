class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        m={}

        res=[]

        for item in nums:
            if item not in m:
                m[item]=1
            else:
                m[item]+=1
                

        while True:
            
            if not m:
                break
                
            row=[]
            
            for i in list(m.keys()):
                if m[i]!=0:
                    row.append(i)
                    m[i]-=1
                    
                else:
                    m.pop(i)
                
            if row:
                res.append(row)
	
        return res   