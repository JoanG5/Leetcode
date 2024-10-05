class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curArr = []

        def dfs(i):
            if len(nums) <= i:
                res.append(curArr.copy())
                return

            curArr.append(nums[i])
            dfs(i + 1)

            curArr.pop()
            dfs(i + 1)

        dfs(0)
        return res    
        