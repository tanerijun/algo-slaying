class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def reverseWords(self, s: str) -> str:
        ls = list(s)

        def reverse(l, r):
            while l < r:
                ls[l], ls[r] = ls[r], ls[l]
                l += 1
                r -= 1

        start = 0
        for end in range(len(s)):
            if s[end] == " ":
                reverse(start, end - 1)
                start = end + 1
            elif end == len(s) - 1:
                reverse(start, end)

        return "".join(s)

    # Time complexity: O(n)
    # Space complexity: O(n)
    def reverseWords1(self, s: str) -> str:
        return " ".join([w[::-1] for w in s.split(" ")])
