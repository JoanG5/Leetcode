class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash = {}
        
        for num in arr:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        
        return len(list(hash.values())) == len(set(hash.values()))