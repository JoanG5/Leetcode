class RandomizedSet(object):

    def __init__(self):
        self.numList = []
        self.numMap = {}

    def insert(self, val):
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        
        return res 
        

    def remove(self, val):
        res = val in self.numMap
        if res:
            i = self.numMap[val]
            lastVal = self.numList[-1]
            self.numList[i] = lastVal
            self.numList.pop()
            self.numMap[lastVal] = i 
            del self.numMap[val]
        return res

    def getRandom(self):
        size = len(self.numList)
        i = random.randint(0, size - 1)
        return self.numList[i]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()