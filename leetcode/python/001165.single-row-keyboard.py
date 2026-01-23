class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1) -> max 26
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = {ch: i for i, ch in enumerate(keyboard)}
        time = 0
        prev_pos = 0
        for ch in word:
            curr_pos = pos[ch]
            time += abs(curr_pos - prev_pos)
            prev_pos = curr_pos
        return time
