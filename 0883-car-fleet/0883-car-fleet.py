class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []

        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        pairs.sort(reverse=True)

        for p, s in pairs:
            rate = (target - p) / s
            stack.append(rate)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
            