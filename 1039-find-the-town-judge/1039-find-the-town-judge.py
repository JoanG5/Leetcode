class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = [0] * (n + 1)
        for i in trust:
            people[i[1]] += 1
            people[i[0]] -= 1
        
        for i in range(1, len(people)):
            if people[i] == n - 1:
                return i
        return -1