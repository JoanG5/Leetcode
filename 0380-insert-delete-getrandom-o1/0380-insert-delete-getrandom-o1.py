class RandomizedSet(object):

    def __init__(self):
        self.map = {}
        self.arr = []

    def insert(self, val):
        res = val not in self.map
        if res:
            self.map[val] = len(self.arr)
            self.arr.append(val)
        return res 

    def remove(self, val):
        res = val in self.map
        if res:
            #[1,2,3]
            #{1:0, 2:1, 3:2}
            # Move end to val change
            # Remove val 
            i = self.map[val]
            lastVal = self.arr[-1]
            self.arr[i] = lastVal
            self.arr.pop()
            self.map[lastVal] = i
            del self.map[val]
        return res

    def getRandom(self):
        i = random.randint(0, len(self.arr) - 1)
        return self.arr[i]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()