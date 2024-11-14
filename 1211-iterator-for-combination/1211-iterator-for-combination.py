class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.length = combinationLength
        self.queue = deque()
        def dfs(i, s):
            if len(s) >= self.length:
                self.queue.append(s[:])
                return
            for j in range(i, len(self.characters)):
                s = s + self.characters[j]
                dfs(j + 1, s)
                s = s[:-1]
        dfs(0, "")

    def next(self) -> str:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return True if self.queue else False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()