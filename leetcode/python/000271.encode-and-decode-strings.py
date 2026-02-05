class Solution:
    # Time complexity: O(n) -> n == total number of characters
    # Space complexity: O(1)
    def encode(self, strs: list[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    # Time complexity: O(n)
    # Space complexity: O(1)
    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res
