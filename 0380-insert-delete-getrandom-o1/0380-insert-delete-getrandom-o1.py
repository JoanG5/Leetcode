class RandomizedSet(object):

    def __init__(self):
        self.randomSet = set()

    def insert(self, val):
        if val in self.randomSet:
            return False
        self.randomSet.add(val)
        return True 
        

    def remove(self, val):
        if val not in self.randomSet:
            return False
        self.randomSet.remove(val)
        return True
        

    def getRandom(self):
        size = len(self.randomSet)
        i = random.randint(0, size)
        return list(self.randomSet)[i]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()