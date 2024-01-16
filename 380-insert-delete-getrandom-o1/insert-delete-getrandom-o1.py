import random

class RandomizedSet(object):

    def __init__(self):
        self.m={}
        self.l=[]

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.m:
            self.m[val] = len(self.l)
            self.l.append(val)
            return True
        
        return False
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.m:            
            pos = self.m[val]

            self.m[self.l[-1]] = pos
            self.l[pos] = self.l[-1]

            self.m.pop(val)
            self.l.pop()

            return True
        
        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.l)


        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()