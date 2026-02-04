class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        total_waiting_time = 0
        chef_idle_tick = 0

        for arrival_tick, prepare_time in customers:
            if chef_idle_tick > arrival_tick:
                order_wait_time = chef_idle_tick - arrival_tick
                chef_idle_tick = chef_idle_tick + prepare_time
            else:
                order_wait_time = 0
                chef_idle_tick = arrival_tick + prepare_time
            total_waiting_time += order_wait_time + prepare_time

        return total_waiting_time / len(customers)
