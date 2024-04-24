class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        map: dict[str, list[str]] = {}

        for s in strs:
            key = "".join(sorted(s))
            if key in map:
                map[key].append(s)
            else:
                map[key] = [s]

        return list(map.values())
