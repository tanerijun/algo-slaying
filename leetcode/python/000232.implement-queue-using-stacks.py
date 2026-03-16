class MyQueue:
    # Time complexity: O(1)
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # Time complexity: O(n)
    def _fill_s2_if_needed(self):
        if len(self.s2) == 0:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())

    # Time complexity: O(1)
    def push(self, x: int) -> None:
        self.s1.append(x)

    # Time complexity: O(n) - Amortized O(1)
    def pop(self) -> int:
        self._fill_s2_if_needed()
        return self.s2.pop()

    # Time complexity: O(n) - Amortized O(1)
    def peek(self) -> int:
        self._fill_s2_if_needed()
        return self.s2[-1]

    # Time complexity: O(1)
    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
