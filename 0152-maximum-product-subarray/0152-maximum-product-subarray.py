class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Multiple negatvies, Even amount give positive, odd will be lower more than likely, unless 1 val
        # 
        # s[i] = the largest product from nums up to i
        # s[0] = nums[0]
        # [2, -3, 6]
        # [2, -6, -36]
        # [2, -3, 6]

        ''' 
        [2, -3, 6]
        [2, -3, 6]
        s[1] = max{
            nums[1],
            s[0] * nums[1]
        }
        s[2] = max{
            nums[2],
            s[1] * nums[2]
        }
        [2, -3, 6]
        [2, -6, -36]
        s[1] = max{
            nums[1],
            abs(s[0] * nums[1])
        }
        s[2] = max{
            nums[2],
            abs(s[1] * nums[2])
        }
        '''

        s1, s2 = [nums[0]] * len(nums), [nums[0]] * len(nums)
        
        for i in range(1, len(nums)):
            s1[i] = max(nums[i], s1[i - 1] * nums[i], s2[i - 1] * nums[i])
            s2[i] = min(nums[i], s1[i - 1] * nums[i], s2[i - 1] * nums[i])

        return max(s1)