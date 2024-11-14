class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def dfs(i, cur):
            if len(cur) == 4 and i == len(s):
                res.append(".".join(cur))
                return
            elif len(cur) == 4 or i == len(s):
                return
            
            for j in range(i + 1, len(s) + 1):
                new_s = s[i:j]
                
                if (len(new_s) > 1 and new_s[0] == "0") or (len(new_s) > 3 or int(new_s) > 255):
                    break
            
                if int(new_s) >= 0 and int(new_s) <= 255:
                    cur.append(new_s)
                    dfs(j, cur)
                    cur.pop()
        dfs(0, [])

        return res