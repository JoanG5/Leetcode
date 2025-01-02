class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        heap = []
        res = []
        for key, value in count.items():
            heapq.heappush(heap,(-value, key))
        
        for _ in range(k):
            val, key = heapq.heappop(heap)
            res.append(key)
        return res
        