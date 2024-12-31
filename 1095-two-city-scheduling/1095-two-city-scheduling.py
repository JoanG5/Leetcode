class Solution(object):
    def twoCitySchedCost(self, costs):
        n = len(costs) / 2
        dif_list = []
        for a, b in costs:
            dif_list.append((abs(a - b), a, b))
       
        dif_list.sort(reverse=True)
        cityA = cityB = res = 0
       
        for _, a, b in dif_list:
            if cityA != n and (a < b or cityB == n):
                cityA += 1
                res += a
            else:
                cityB += 1
                res += b
            
        return res
        