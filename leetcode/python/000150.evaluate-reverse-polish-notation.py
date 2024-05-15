class Solution:
	# Time complexity: O(n)
	# Space complexity: O(n)
	def evalRPN(self, tokens: list[str]) -> int:
		stack = []

		for token in tokens:
			stack.append(token)

			if stack[-1] in ["+", "-", "*", "/"]:
				operator = stack.pop()
				b = int(stack.pop())
				a = int(stack.pop())
				res = a + b if operator == "+" else \
					a - b if operator == "-" else \
					a * b if operator == "*" else \
					a / b if operator == "/" else None
				stack.append(res)

		return int(stack[-1])
