class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def isPathCrossing(self, path: str) -> bool:
        visited = set([(0, 0)])
        cur = (0, 0)
        for d in path:
            dx, dy = 0, 0
            if d == "N":
                dy = 1
            elif d == "S":
                dy = -1
            elif d == "E":
                dx = 1
            elif d == "W":
                dx = -1
            cur = (cur[0] + dx, cur[1] + dy)
            if cur in visited:
                return True
            visited.add(cur)
        return False
