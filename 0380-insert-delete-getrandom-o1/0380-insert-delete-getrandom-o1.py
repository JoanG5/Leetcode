class RandomizedSet:

    def __init__(self):
        self.randArr = []
        self.randSet = {}

    def insert(self, val: int) -> bool:
        res = not val in self.randSet
        if res:
            self.randSet[val] = len(self.randArr)
            self.randArr.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.randSet
        #[1, 2, 3]
        #[1: 0, 2: 1, 3: 2]
        if res:
            lastInd = len(self.randArr) - 1
            lastVal = self.randArr[-1]
            curInd = self.randSet[val]
            self.randArr[lastInd], self.randArr[curInd] = self.randArr[curInd], self.randArr[lastInd]
            self.randSet[lastVal] = curInd
            del self.randSet[val]
            self.randArr.pop()
        
        return res

    def getRandom(self) -> int:
        size = len(self.randArr)
        n = random.randint(0, size - 1)
        return self.randArr[n]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()