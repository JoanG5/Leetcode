class Solution(object):
    def twoCitySchedCost(self, costs):
        n = len(costs) // 2
        dif_cost = []
        for a, b in costs:
            dif = abs(a - b)
            dif_cost.append((dif, a, b))
        dif_cost.sort(reverse=True)
        cityA = cityB = res = 0

        for _, a, b in dif_cost:
            if cityA != n and (cityB == n or a <= b):
                res += a
                cityA += 1
            else:
                res += b
                cityB += 1
        
        return res
        