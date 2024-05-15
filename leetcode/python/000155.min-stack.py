class MinStack:

	# O(1)
	def __init__(self):
		self.min_stack = []
		self.array = []

	# O(1)
	def push(self, val: int) -> None:
		self.array.append(val)
		if not self.min_stack or val <= self.getMin():
			self.min_stack.append(val)

	# O(1)
	def pop(self) -> None:
		popped = self.array.pop()
		if popped == self.getMin():
			self.min_stack.pop()

	# O(1)
	def top(self) -> int:
		return self.array[-1]

	# O(1)
	def getMin(self) -> int:
		return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
