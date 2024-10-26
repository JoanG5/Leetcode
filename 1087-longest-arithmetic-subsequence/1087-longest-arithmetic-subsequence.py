class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        check = {}
        for r in range(len(nums)):
            l = 0
            for l in range(0, r):
                dif = nums[r] - nums[l]
                if (l, dif) in check:
                    check[(r, dif)] = check[(l, dif)] + 1
                else:
                    check[(r, dif)] = 2
                l += 1
        
        return max(check.values())