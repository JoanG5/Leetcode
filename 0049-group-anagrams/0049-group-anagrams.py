class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for word in strs:
            bucket = [0] * 26
            for i in word:
                bucket[ord(i) - ord("a")] += 1
            bucket = tuple(bucket)
            if bucket in res:
                res[bucket].append(word)
            else:
                res[bucket] = [word]

        return res.values()   