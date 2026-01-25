from collections import defaultdict


class Solution:
    # Time complexity: O(n * k) -> Where n is the length of strings and k is the maximum length of a string in strings.
    # Space complexity: O(n * k)
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        group_map = defaultdict(list)

        for s in strings:
            diffs = []
            for i in range(len(s) - 1):
                diffs.append(
                    str((ord(s[i]) - ord(s[i + 1])) % 26)
                )  # in other langs: ((ord(s[i]) - ord(s[i + 1])) % 26 + 26) % 26

            group_map[",".join(diffs)].append(s)

        return list(group_map.values())
