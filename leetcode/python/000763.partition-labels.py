class Solution:
    # Time complexity: O(n)
    # Space complexity: O(26) == O(1)
    def partitionLabels(self, s: str) -> list[int]:
        last_index_map = {}
        for i in range(len(s)):
            last_index_map[s[i]] = i

        res = []
        window_size, end_index = 0, 0

        for i in range(len(s)):
            window_size += 1
            end_index = max(end_index, last_index_map[s[i]])
            if i == end_index:
                res.append(window_size)
                window_size = 0

        return res
