class Solution:
    # Time complexity: O(n(log(n)) + m(log(m)))
    # Space complexity: O(n + m) - from sorting algorithm
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        i = j = 0
        while i < len(players) and j < len(trainers):
            if trainers[j] < players[i]:
                j += 1
            else:
                i += 1
                j += 1
        return i
