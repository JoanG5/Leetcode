class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Base case
        # # If current i >= len(digits)
        if len(digits) <= 0:
            return []
        res = []
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7":"pqrs", "8":"tuv", "9": "wxyz"}

        def helper(i, s):
            if i >= len(digits):
                res.append(s[:])
                return
            for j in phone[digits[i]]:
                helper(i + 1, s + j)
        
        helper(0, "")

        return res