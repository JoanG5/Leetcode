class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # Has to be size k
        # May end up removing more than need be
        stack = []
        n = len(nums)

        for i in range(n):
            while stack and nums[i] < stack[-1] and (n - i) != k - len(stack) :
                stack.pop()
            if len(stack) != k:
                stack.append(nums[i])
        
        return stack 