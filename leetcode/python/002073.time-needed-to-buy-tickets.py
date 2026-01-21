class Solution:
    # Time complexity: O(n * m) -> n = len(tickets), m = tickets[k]
    # Space complexity: O(1)
    # Simulation
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time = 0
        i = 0
        while True:
            if tickets[i] != 0:
                time += 1
                tickets[i] -= 1
                if tickets[i] == 0 and i == k:
                    return time

            i += 1
            i %= len(tickets)

    # Time complexity: O(n)
    # One pass
    # Calculate exactly how many tickets each person contributes to the total wait time based on their position relative to k.
    # People before or at k (i <= k):
    #     Buy tickets before k in every round.
    #     They will contribute either their total tickets or k's total tickets (whichever is smaller) to the time.
    # People after k (i > k):
    #     Buy tickets after k in every round. However, in the very last round (when k buys their last ticket),
    #     the process stops immediately. People behind k don't get to buy a ticket in that final round.
    def timeRequiredToBuy1(self, tickets: list[int], k: int) -> int:
        time = 0

        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], tickets[k])
            else:
                time += min(tickets[i], tickets[k] - 1)

        return time
