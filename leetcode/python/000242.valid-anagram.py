class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_map = {}
        t_char_map = {}

        for ch in s:
            s_char_map[ch] = s_char_map.get(ch, 0) + 1

        for ch in t:
            t_char_map[ch] = t_char_map.get(ch, 0) + 1

        return s_char_map == t_char_map

    # Time complexity: O(n)
    # Space complexity: O(n)
    def isAnagram2(self, s: str, t: str) -> bool:
        map = {}

        for ch in s:
            map[ch] = map.get(ch, 0) + 1

        for ch in t:
            map[ch] = map.get(ch, 0) - 1

        for v in map.values():
            if v != 0:
                return False

        return True
