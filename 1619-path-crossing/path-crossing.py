class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        
        x=0
        y=0
        dic={(0,0):1}
        
        for i in range(len(path)):

            if path[i]=="N":
                y+=1                  
            elif path[i]=="S":
                y-=1
            elif path[i]=="E":
                x+=1
            else:
                x-=1    
                
            if (x,y) in dic:
                    return True    
            dic[(x,y)]=1

        return False
