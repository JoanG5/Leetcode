class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_strs = [str(x) for x in nums]

        def compare(a, b):
            if a + b > b + a: return - 1
            elif a + b < b + a: return 1
            else: return 0
        
        nums_strs.sort(key=cmp_to_key(compare))
        
        if nums_strs[0] == '0': return '0' 
        
        return ''.join(nums_strs)