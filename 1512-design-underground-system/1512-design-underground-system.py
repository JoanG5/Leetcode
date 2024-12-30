class UndergroundSystem(object):

    def __init__(self):
        self.time = {}
        self.avg = {}

    def checkIn(self, id, stationName, t):
        self.time[id] = (stationName, t)
        

    def checkOut(self, id, stationName, t):
        start, startTime = self.time[id]
        time = t - startTime
        if not (start, stationName) in self.avg:
            self.avg[(start, stationName)] = [0, 0]
        self.avg[(start, stationName)][0] += time
        self.avg[(start, stationName)][1] += 1
        

    def getAverageTime(self, startStation, endStation):
        return float(self.avg[(startStation, endStation)][0]) / float(self.avg[(startStation, endStation)][1]) 
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)