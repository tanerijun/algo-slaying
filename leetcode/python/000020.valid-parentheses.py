class Solution:
	# Time complexity: O(n)
	# Space complexity: O(n)
	def isValid(self, s: str) -> bool:
		stack = []
		for ch in s:
			match ch:
				case "[":
					stack.append("]")
				case "(":
					stack.append(")")
				case "{":
					stack.append("}")
				case _:
					if not stack or not stack.pop() == ch:
						return False
		return len(stack) == 0
