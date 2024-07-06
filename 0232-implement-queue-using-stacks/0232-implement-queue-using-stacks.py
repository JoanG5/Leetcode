class MyQueue:

    def __init__(self):
        self.stack = []
        self.flip = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while self.stack:
            self.flip.append(self.stack.pop())
        val = self.flip.pop()
        while self.flip:
            self.stack.append(self.flip.pop())
        return val

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not self.stack and not self.flip
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()