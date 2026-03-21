from collections import Counter


class Solution:
    # Time complexity: O(n * n!)
    # Space complexity: O(n)
    def numTilePossibilities(self, tiles: str) -> int:
        counter = Counter(tiles)

        def backtrack():
            res = 0
            for c in counter:
                if counter[c] > 0:
                    counter[c] -= 1
                    res += 1
                    res += backtrack()
                    counter[c] += 1
            return res

        return backtrack()

    # Time complexity: O(n * n!)
    # Space complexity: O(n)
    def numTilePossibilities2(self, tiles: str) -> int:
        sorted_tiles = sorted(tiles)
        n = len(sorted_tiles)
        used = set()
        res = 0

        def backtrack():
            nonlocal res
            for i in range(n):
                if i in used:
                    continue
                if (
                    i > 0
                    and sorted_tiles[i] == sorted_tiles[i - 1]
                    and i - 1 not in used
                ):
                    continue
                used.add(i)
                res += 1
                backtrack()
                used.remove(i)

        backtrack()
        return res
