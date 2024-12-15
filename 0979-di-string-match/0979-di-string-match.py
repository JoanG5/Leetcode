class Solution(object):
    def diStringMatch(self, s):
        start, end = 0, len(s)
        res = []
        for i in s:
            if i == "I":
                res.append(start)
                start += 1
            else:
                res.append(end)   
                end -= 1
        res.append(start)

        return res      