class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def minOperations(self, logs: list[str]) -> int:
        stack = []
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log == "./":
                continue
            else:
                stack.append(log)
        return len(stack)

    # Time complexity: O(n)
    # Space complexity: O(1)
    def minOperations1(self, logs: list[str]) -> int:
        level = 0
        for log in logs:
            if log == "../":
                if level > 0:
                    level -= 1
            elif log == "./":
                continue
            else:
                level += 1
        return level
