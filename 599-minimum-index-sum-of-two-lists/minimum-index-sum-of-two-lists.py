class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        common={}

        for s in list1:
            if s in list2:
                i=list1.index(s)
                j=list2.index(s)       
                common[s]=i+j


        temp=min(common.values())
        
        res=[]
        for key in common:
            if common[key]==temp:
                res.append(key)

        return res