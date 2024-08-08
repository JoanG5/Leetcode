class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        streak = 1
        for num in num_set:
            if not num + 1 in num_set:
                current = num
                while current - 1 in num_set:
                    streak += 1
                    current -= 1
            res = max(res, streak)
            streak = 1
        
        return res
            
