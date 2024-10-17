class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        # Go through the list
        # If 60 - (cur % 60)   is NOT in the hash then add cur to it
        # If it is then add one to the res 
        visited = {}
        res = 0

        for num in time:
            cur = num % 60
            complement = (60 - cur) % 60
            if complement in visited:
                res += visited[complement]
            if cur in visited:
                visited[cur] += 1
            else: 
                visited[cur] = 1
        return res


