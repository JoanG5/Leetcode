class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.set = {}

    def insert(self, val: int) -> bool:
        res = not val in self.set
        if res:
            self.arr.append(val)
            i = len(self.arr) - 1
            self.set[val] = i
        
        return res

    def remove(self, val: int) -> bool:
        res = val in self.set
        if res:
            i = self.set[val]
            lastVal = self.arr[-1]
            self.arr[i] = lastVal
            self.arr.pop()
            self.set[lastVal] = i
            del self.set[val]
        
        return res

    def getRandom(self) -> int:
        size = len(self.arr)
        i = random.randint(0, size - 1)
        return self.arr[i] 


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()