class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1) -> max 26
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        range_map = {}

        for i, ch in enumerate(s):
            if ch not in range_map:
                range_map[ch] = [i, None]
            else:
                range_map[ch][1] = i

        res = -1
        for v in range_map.values():
            l, r = v
            if r:
                res = max(res, r - l - 1)

        return res

    # Time complexity: O(n)
    # Space complexity: O(1) -> max 26
    def maxLengthBetweenEqualCharacters2(self, s: str) -> int:
        last_index_map = {}
        for i in range(len(s)):
            last_index_map[s[i]] = i

        res = -1
        for i in range(len(s)):
            if s[i] in last_index_map and last_index_map[s[i]] != i:
                res = max(res, last_index_map[s[i]] - i - 1)

        return res
