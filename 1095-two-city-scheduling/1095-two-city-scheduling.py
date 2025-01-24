class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff_arr = []
        n = len(costs)
        for a, b in costs:
            diff = abs(a - b)
            diff_arr.append((diff, a, b))
        
        diff_arr.sort(reverse=True)
        res = a_count = b_count = 0
        
        for _, a, b in diff_arr:
            if a_count < n / 2 and (a < b or b_count == n / 2):
                a_count += 1
                res += a
            else:
                b_count += 1
                res += b
                
        return res 
