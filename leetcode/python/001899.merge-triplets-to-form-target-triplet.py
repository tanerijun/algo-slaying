class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    # Intuition:
    # - We can't "undo" a max operation. Once we merge triplets and a position becomes too large, we can never make it smaller.
    # - So for each position in the target:
    #    - We need to find at least one triplet that contributes the target value at that position
    #    - That same triplet must not "ruin" other positions by being too large
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        x = y = z = False
        for t in triplets:
            x |= t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2]
            y |= t[0] <= target[0] and t[1] == target[1] and t[2] <= target[2]
            z |= t[0] <= target[0] and t[1] <= target[1] and t[2] == target[2]
            if x and y and z:
                return True
        return False
