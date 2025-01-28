class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = []
        count = {}

        for c in cpdomains:
            split_domain = c.split()
            curNum = split_domain[0]
            website = split_domain[1].split(".")
            cur = ""
            for domain in website[::-1]:
                cur = domain + cur
                count[cur] = count.get(cur, 0) + int(curNum)
                cur = '.' + cur

        for k, v in count.items():
            res.append(f"{v} {k}")

        return res