class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        m={}
        count=0

        for num in tasks:

            if num in m:
                m[num]+=1

            else:
                m[num]=1

        for element in m:

            if m[element]==1:
                return -1
            
            if m[element]%3==0:
                count+=m[element]/3
            
            else:
                count+=m[element]/3+1       
            
        return count