class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        point = 0

        for letter in t:
            if point >= len(s):
                return True

            if letter == s[point]:
                point += 1

        return len(s) <= point