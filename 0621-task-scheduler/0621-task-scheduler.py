class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        bucket = [0] * 26
        for task in tasks:
            bucket[ord(task) - ord('A')] += 1

        bucket.sort()
        maxTask = bucket.pop()
        num_of_idle =  n * (maxTask-1)

        while bucket and num_of_idle > 0:
            num_of_idle -= min(maxTask - 1, bucket.pop())
        
        num_of_idle = max(0, num_of_idle)

        return num_of_idle + len(tasks)