class Solution:
    # Time complexity: O(n(log(n)))
    # Space complexity: O(n)
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        return [
            el[0]
            for el in sorted(zip(names, heights), key=lambda x: x[1], reverse=True)
        ]
