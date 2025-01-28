class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, arr, total):
            if total == target:
                res.append(arr[:])
                return
            if total > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                arr.append(candidates[j])
                dfs(j + 1, arr, total + candidates[j])
                arr.pop()

        dfs(0, [], 0)
        return res