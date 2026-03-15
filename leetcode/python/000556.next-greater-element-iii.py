class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))

        # Find first dip from the right (pivot)
        pivot_idx = -1
        for i in range(len(digits) - 1, 0, -1):
            if digits[i - 1] < digits[i]:
                pivot_idx = i - 1
                break

        # Entire number is descending (no answer)
        if pivot_idx == -1:
            return -1

        # Find rightmost digit in suffix that beat pivot
        swap_target_idx = -1
        for i in range(len(digits) - 1, pivot_idx, -1):
            if digits[i] > digits[pivot_idx]:
                swap_target_idx = i
                break

        # Swap
        digits[pivot_idx], digits[swap_target_idx] = (
            digits[swap_target_idx],
            digits[pivot_idx],
        )

        # Reverse suffix
        digits[pivot_idx + 1 :] = digits[pivot_idx + 1 :][::-1]

        res = int("".join(digits))
        return res if res <= 2**31 - 1 else -1
