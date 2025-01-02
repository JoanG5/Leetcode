class Solution(object):
    def frequencySort(self, nums):
        counter = Counter(nums)

        nums.sort(key=lambda num:(counter[num], -num))
        return nums
        