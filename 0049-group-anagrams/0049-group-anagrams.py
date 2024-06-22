class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            bucket = [0] * 26
            for letter in word:
                bucket[ord(letter) - ord("a")] += 1
            if tuple(bucket) in res:
                res[tuple(bucket)].append(word)
            else: 
                res[tuple(bucket)] = [word]
        
        return res.values()
