class Solution:
	# Time complexity: O(n)
	# Space complexity: O(n)
	def isValid(self, s: str) -> bool:
		stack = []
		for ch in s:
			match ch:
				case "]":
					if not stack or not stack.pop() == "[":
						return False
				case ")":
					if not stack or not stack.pop() == "(":
						return False
				case "}":
					if not stack or not stack.pop() == "{":
						return False
				case _:
					stack.append(ch)
		return len(stack) == 0
