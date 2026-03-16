class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def makeGood(self, s: str) -> str:
        stack: list[str] = []
        for ch in s:
            if (
                stack
                and ch.lower() == stack[-1].lower()
                and (
                    (ch.isupper() and stack[-1].islower())
                    or (ch.islower() and stack[-1].isupper())
                )
            ):
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
