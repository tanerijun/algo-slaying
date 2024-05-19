class Solution:
	# Time complexity: O(n)
	# Space complexity: O(n)
	def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
		position_and_speed = sorted(zip(position, speed), reverse=True, key=lambda tup: tup[0])

		res = 0
		blocker_time_to_target = 0

		for pos, spd in position_and_speed:
			time_to_target = (target - pos) / spd
			if time_to_target > blocker_time_to_target:
				blocker_time_to_target = time_to_target
				res += 1

		return res

	# Time complexity: O(n)
	# Space complexity: O(n) - slightly more space efficient then carFleet
	def carFleet2(self, target: int, position: list[int], speed: list[int]) -> int:
		# Sort the indices based on position in descending order
		sorted_indices = sorted(range(len(position)), key=lambda i: -position[i])

		res = 0
		blocker_time_to_target = 0

		for i in sorted_indices:
			time_to_target = (target - position[i]) / speed[i]
			if time_to_target > blocker_time_to_target:
				blocker_time_to_target = time_to_target
				res += 1
		return res

	# Time complexity: O(n)
	# Space complexity: O(n) - using stack
	def carFleet3(self, target: int, position: list[int], speed: list[int]) -> int:
		position_and_speed = sorted(zip(position, speed), reverse=True, key=lambda tup: tup[0])
		stack = []
		for pos, spd in position_and_speed:
			time_to_target = (target - pos) / spd
			stack.append(time_to_target)
			# Check for collision
			if len(stack) >= 2 and stack[-1] <= stack[-2]:
				stack.pop()
		return len(stack)
