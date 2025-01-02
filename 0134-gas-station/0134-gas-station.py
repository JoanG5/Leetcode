class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_gas = cur = start = 0

        for i in range(len(gas)):
            dif = gas[i] - cost[i]
            total_gas += dif
            cur += dif

            if cur < 0:
                start = i + 1
                cur = 0
        
        return start if total_gas >= 0 else - 1
        
