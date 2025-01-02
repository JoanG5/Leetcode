class RandomizedSet(object):

    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val):
        res = val not in self.map
        if res:
            self.map[val] = len(self.list)
            self.list.append(val)
        return res
        

    def remove(self, val):
        res = val in self.map
        if res:
            i = self.map[val]
            lastVal = self.list[-1]
            self.list[i] = lastVal
            self.list.pop()
            self.map[lastVal] = i 
            del self.map[val]
        return res
        

    def getRandom(self):
        size = len(self.list)
        i = random.randint(0, size - 1)
        return self.list[i]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()