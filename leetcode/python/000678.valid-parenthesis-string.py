class Solution:
    # Time complexity: O(n)
    # Space complexity: O
    def checkValidString(self, s: str) -> bool:
        min_open = 0  # minimum possible unmatched '(' brackets (pessimistic view)
        max_open = 0  # maximum possible unmatched '(' brackets (optimistic view)

        for ch in s:
            if ch == "(":
                min_open += 1
                max_open += 1
            elif ch == ")":
                min_open -= 1
                max_open -= 1
            else:
                # For min_open (pessimistic): use '*' as ')' or empty to minimize opens
                # - If we have open brackets, treat '*' as ')' to close one
                # - If we don't have open brackets, treat '*' as empty
                #   (this causes min_open to go negative, but will be clamped to 0 below)
                min_open -= 1
                # For max_open (optimistic): use '*' as '(' to maximize opens
                # This gives us the most flexibility for future ')' brackets
                max_open += 1

            if max_open < 0:  # too many ')'
                return False

            # Clamp min_open to 0 because we can't have negative open brackets
            # If min_open would go negative, it means we're treating '*' as ')'
            # when there's no '(' to close, so we treat '*' as empty instead
            # Example: "*)" → after '*': min_open = -1 → clamp to 0
            #                 after ')': min_open = -1 → would fail on next check
            min_open = max(0, min_open)

        # Final check: Can we achieve exactly 0 unmatched open brackets?
        # Our range of possibilities is [min_open, max_open]
        # We need 0 to be in this range, which means min_open <= 0 <= max_open
        # Since we already know min_open >= 0 (due to clamping) and max_open >= 0 (from checks above),
        # We need min_open == 0 exactly
        return min_open == 0
