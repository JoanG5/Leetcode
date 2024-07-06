class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        def helper(i, distance):
            if i < 0 or i > len(s) - 1 or distance >= res[i]:
                return
            
            res[i] = distance
            helper(i + 1, distance + 1)
            helper(i - 1, distance + 1)

        res = [len(s) - 1 for _ in range(len(s))]
        for i in range(len(s)):
            if s[i] == c:
                helper(i, 0)
        
        return res