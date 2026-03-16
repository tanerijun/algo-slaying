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

    # Time complexity: O(n)
    # Space complexity: O(n)
    def makeGood1(self, s: str) -> str:
        stack: list[str] = []
        for ch in s:
            if stack and ch != stack[-1] and ch.lower() == stack[-1].lower():
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)

    # Time complexity: O(n)
    # Space complexity: O(n)
    def makeGood2(self, s: str) -> str:
        stack: list[str] = []
        for ch in s:
            # The difference between a lowercase letter and its uppercase counterpart is exactly 32
            # (e.g., 'a' is 97 and 'A' is 65)
            if stack and abs(ord(ch) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
