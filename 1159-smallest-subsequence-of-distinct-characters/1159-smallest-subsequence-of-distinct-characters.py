class Solution:
    def smallestSubsequence(self, s: str) -> str:
        visit = set()
        count = Counter(s)
        stack = []
        for i in range(len(s)):
            count[s[i]] -= 1
            if not s[i] in visit:
                while stack and stack[-1] > s[i] and count[stack[-1]] != 0:
                    top = stack.pop()
                    visit.remove(top)
                stack.append(s[i])
                visit.add(s[i])
            
        return "".join(stack)