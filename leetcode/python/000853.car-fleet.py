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
