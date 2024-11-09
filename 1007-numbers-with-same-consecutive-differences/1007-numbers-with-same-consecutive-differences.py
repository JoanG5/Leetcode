class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        def dfs(i, cur, total):
            total = total * 10 + cur
            if i >= n - 1:
                res.append(total)
                return
            if k == 0:
                dfs(i + 1, cur + k, total)
            else:
                if cur + k < 10:
                    dfs(i + 1, cur + k, total)
                if cur - k >= 0:
                    dfs(i + 1, cur - k, total)
        
        for i in range(1, 10):
            dfs(0, i, 0)
        return res

