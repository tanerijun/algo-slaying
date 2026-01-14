from collections import defaultdict


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def destCity(self, paths: list[list[str]]) -> str:
        graph = defaultdict(list)
        for src, dst in paths:
            graph[src].append(dst)

        for src, dst in paths:
            if src not in graph:
                return src
            if dst not in graph:
                return dst
        return ""  # impossible
