class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict) 
        memo = [True] + [False] * len(s)
        for i in range(len(s)):
            if memo[i]:
                for j in range(i + 1, len(s) + 1): 
                    if s[i:j] in wordSet: memo[j] = True     
        return memo[-1]