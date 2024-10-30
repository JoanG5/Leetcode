class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        pair = {}

        for num in arr:
            comp = num % k
            pair[comp] = pair.get(comp, 0) + 1

        for comp, count in pair.items():
            if comp == 0:
                if count % 2 != 0:
                    return False
            else:
                if pair.get(comp, 0) != pair.get(k - comp, 0):
                    return False
        return True
