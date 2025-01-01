class OrderedStream(object):

    def __init__(self, n):
        self.list = [""] * n
        self.cur = 0

    def insert(self, idKey, value):
        res = []
        self.list[idKey - 1] = value
        while self.cur < len(self.list) and self.list[self.cur] != "":
            res.append(self.list[self.cur])
            self.cur += 1
        
        return res

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)