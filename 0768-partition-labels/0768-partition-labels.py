class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = {}
        for l in s:
            counter[l] = counter.get(l, 0) + 1

        res = []
        visited = set()
        curSum = 0 
        start = 0
        for i in range(len(s)):
            if s[i] not in visited:
                curSum += counter[s[i]]
                visited.add(s[i])
            counter[s[i]] -= 1
            curSum -= 1
            if curSum == 0:
                res.append(i - start + 1)
                start = i + 1
        
        return res 